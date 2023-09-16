# -*- coding: utf-8 -*-
import os
from taipy.gui import notify, Markdown
from supabase import create_client, Client
import pandas as pd
from pages.ppt import create_presentation


def return_dados():
    tbl = None
    try:
        tbl = supabase.table("questoes").select("*").order("id").execute()
        df = pd.DataFrame(tbl.data)
        df["label"] = "Questão " + df["id"].astype(str)
        df.set_index("id", inplace=True)
        df.index.name = "index"
    except:
        pass
    return df


# Definição de Variável
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)
dados = return_dados()
link = ""
content = None
download_active = False
display_resultado = None
display_index = None


def refresh_dados(state):
    state.dados = return_dados()


def exportar_ppt(state):
    create_presentation(state.dados, "questoes.pptx")
    state.content = open("questoes.pptx", "rb").read()
    state.download_active = True
    state.link = "questoes.pptx"
    notify(state, "success", "Powerpoint Gerado!")


def download_start(state):
    state.download_active = False


def delete_questao(state, var_name, action, payload):
    data = supabase.table("questoes").delete().eq("id", payload["index"]).execute()
    state.dados = return_dados()
    state.download_active = False
    notify(state, "success", "Questão removida!")


def show_resultado(state, var_name, action, payload):
    state.display_index = payload["index"]
    state.display_resultado = state.dados["resultado"][payload["index"]]


def salvar_questao(state):
    data = (
        supabase.table("questoes")
        .update({"resultado": state.display_resultado})
        .eq("id", state.display_index)
        .execute()
    )
    state.dados = return_dados()
    state.download_active = False
    notify(state, "success", "Questão alterada!")


# Definição Pagina
tbl_q_md = Markdown(
    """<|container|
        
# Lista de Questões Geradas

<|layout|columns=1fr|gap=5px|class_name=card|
<|c1|
<center><|Atualizar|button|on_action=refresh_dados|> <|Exportar|button|on_action=exportar_ppt|> 
<|{content}|file_download|label=Download|name={link}|active={download_active}|on_action=download_start|></center>
|>
|>
<|layout|columns=475px 1fr|gap=5px|class_name=card|
<|c2|
<|{dados}|table|page_size=15|columns=label;nivel;tipo|class_name=fullwidth|editable=True|on_delete=delete_questao|on_action=show_resultado|>
|>
<|c3|
<|{display_resultado}|input|label="Questão"|multiline=true|class_name=fullwidth|>
<br/>
<center><|Salvar|button|on_action=salvar_questao|></center>
|>
|>
|>
"""
)
