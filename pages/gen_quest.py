# -*- coding: utf-8 -*-
import os
from taipy.gui import Gui, notify, Markdown
from supabase import create_client, Client

import pages.oai as oai


def send_database(state, id, action):
    try:
        url: str = os.environ.get("SUPABASE_URL")
        key: str = os.environ.get("SUPABASE_KEY")
        supabase: Client = create_client(url, key)
        tbl = supabase.table("questoes")
        tbl.insert(
            {
                "area": state.area,
                "tipo": state.tipo,
                "nivel": state.nivel,
                "prompt": state.prompt,
                "resultado": state.resultado,
            }
        ).execute()
        notify(state, "sucesso", "Questão salva!")
        state.salvar = False
    except:
        notify(state, "error", "Erro ao salvar a questão")


def send_question(state, id, action):
    state.resultado = "Waiting ..."
    resultado = None
    if state.objetivo == "":
        notify(state, "error", "Defina a ementa da questão!")
        return None

    openai = oai.Openai()
    state.prompt = openai.build_prompt(
        state.nivel,
        state.objetivo,
        state.tipo,
        state.area,
        state.tem_introducao,
        state.tem_resposta,
    )
    openai.set_key(os.getenv("OAI_API_KEY"))
    flagged = openai.moderate(state.prompt)

    if flagged:
        notify(state, "error", "Problema no prompt")
    else:
        resultado = openai.complete(state.prompt).strip().replace('"', "")

    state.resultado = resultado
    notify(state, "success", "Questão criada!")
    state.salvar = True


# Definição de Variável
area = "Gestão de Dados"
nivel = "Fácil"
tipo = "Escolha Simples"
objetivo = "Lógica de Programação com Python: if, for, dicionários e listas"
tem_resposta = "Sim"
tem_introducao = "Sim"
lkp_tipos = eval(os.getenv("QST_TIPOS"))
lkp_niveis = eval(os.getenv("QST_NIVEIS"))
lkp_areas = eval(os.getenv("QST_AREAS"))
salvar = False

prompt = ""
resultado = ""

# Definição Pagina
gen_q_md = Markdown(
    """<|container|
    
# Gerar de Questões

<|layout|columns=1fr 250px|gap=5px|class_name=card|
<|c1|
**Ementa**
|>
<|c2|
**Parâmetros**
|>
<|c3|
<|{area}|selector|lov={lkp_areas}|dropdown|label=Selecione a Área da Questão|class_name=fullwidth|>
<br/>
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
<center><|Gerar Questão|button|on_action=send_question|> <|Salvar Questão|button|on_action=send_database|active={salvar}|></center>
<br/>
<br/>
<|{prompt}|input|multiline|label=Prompt|class_name=fullwidth|>
<br/>
<|{resultado}|input|multiline|label=Resultado|class_name=fullwidth|>
|>
"""
)
