# -*- coding: utf-8 -*-
import os
from taipy.gui import Gui, notify, Markdown
from supabase import create_client, Client

import pages.oai as oai


# Define functions
def generate_text(state):
    base_prompt = f"""Você é um especialista em Ciência de Dados.
  Elabore uma questão de nível {state.nivel} sobre a ementa descrita abaixo:
  Ementa: {state.objetivo}
  A questáo deve ser do tipo: {state.tipo}
  A questão deve ser estruturada da seguinte forma:"""

    if state.tem_introducao == "Sim":
        base_prompt = base_prompt + """\n- Apresenta-se uma introdução ao conteúdo"""

    base_prompt = base_prompt + """\n- Apresenta-se o enunciado da questão"""

    if state.tipo in ["Escolha Simples", "Escolha Múltipla"]:
        base_prompt = base_prompt + """\n- Apresentam-se 5 alternativas de resposta"""

    if state.tipo in ["Completar as Lacunas"]:
        base_prompt = (
            base_prompt
            + """\n- Apresenta-se uma frase que deve conter até 3 lacunas representadas por ___
        - Apresentam-se 5 alternativas de resposta com os termos para completar as lacunas"""
        )

    if state.tem_resposta == "Sim":
        base_prompt = (
            base_prompt
            + """\n- Apresenta-se a resposta correta, e explique a resposta."""
        )

    state.prompt = base_prompt
    # openai configured and check if text is flagged
    openai = oai.Openai()
    openai.set_key(os.getenv("OAI_API_KEY"))
    flagged = openai.moderate(base_prompt)

    if flagged:
        notify(state, "error", "Problema no prompt")
        return None
    else:
        resultado = openai.complete(base_prompt).strip().replace('"', "")
        return resultado


def send_database(state, id, action):
    try:
        url: str = os.environ.get("SUPABASE_URL")
        key: str = os.environ.get("SUPABASE_KEY")
        supabase: Client = create_client(url, key)
        tbl = supabase.table("questoes")
        tbl.insert(
            {
                "tipo": state.tipo,
                "nivel": state.nivel,
                "prompt": state.prompt,
                "resultado": state.resultado,
            }
        ).execute()
        notify(state, "sucesso", "Questão salva!")
    except:
        notify(state, "error", "Erro ao salvar a questão")


def send_question(state, id, action):
    state.resultado = "Waiting ..."
    if state.objetivo == "":
        notify(state, "error", "Defina a ementa da questão!")
        return None

    state.resultado = generate_text(state)
    notify(state, "success", "Questão criada!")


# Definição de Variável
nivel = "Fácil"
tipo = "Escolha Simples"
objetivo = "Lógica de Programação com Python: if, for, dicionários e listas"
tem_resposta = "Sim"
tem_introducao = "Sim"
lkp_tipos = eval(os.getenv("QST_TIPOS"))
lkp_niveis = eval(os.getenv("QST_NIVEIS"))

prompt = ""
resultado = ""

# Definição Pagina
gen_q_md = Markdown(
    """<|container|
    
# Gerador de Questões - Data Science

<|layout|columns=1fr 250px|gap=5px|class_name=card|
<|c1|
**Ementa**
|>
<|c2|
**Parâmetros**
|>
<|c3|
<|{objetivo}|input|label="Digite a ementa que a questão deve abordar:"|multiline=true|class_name=fullwidth|>
|>
<|c4|
<|{tipo}|selector|lov={lkp_tipos}|dropdown|label=Selecione o Tipo da Questão|>
<br/>
<|{nivel}|selector|lov={lkp_niveis}|dropdown|label=Selecione o Nível da Questão|>
<br/>
Inclui Introdução?<br/><|{tem_introducao}|toggle|lov=Sim;Não|>
<br/>
Inclui Resposta?<br/><|{tem_resposta}|toggle|lov=Sim;Não|>
|>
|>
---
<br/>
<center><|Gerar Questão|button|on_action=send_question|> <|Salvar Questão|button|on_action=send_database|></center>
<br/>
<br/>
<|{prompt}|input|multiline|label=Prompt|class_name=fullwidth|>
<br/>
<|{resultado}|input|multiline|label=Resultado|class_name=fullwidth|>
|>
"""
)
