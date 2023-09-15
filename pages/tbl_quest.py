# -*- coding: utf-8 -*-
import os
from taipy.gui import notify, Markdown
from supabase import create_client, Client
import pandas as pd
from pages.ppt import create_presentation


def return_dados():
    tbl = None
    try:
        tbl = supabase.table("questoes").select("*").execute()
        df = pd.DataFrame(tbl.data)
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
    print(data)
    state.dados = return_dados()
    print(payload["index"])


# Definição Pagina
tbl_q_md = Markdown(
    """<|container|
        
# Lista de Questões Geradas

<|layout|columns=1fr|gap=5px|class_name=card|
<|c1|
<center><|Atualizar|button|on_action=refresh_dados|> <|Exportar|button|on_action=exportar_ppt|> 
<|{content}|file_download|label=Download|name={link}|active={download_active}|on_action=download_start|></center>
|>
<|c3|
<|{dados}|table|page_size=2|class_name=fullwidth|editable=True|on_delete=delete_questao|>
|>
|>
|>
"""
)
