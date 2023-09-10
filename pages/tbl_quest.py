# -*- coding: utf-8 -*-
import os
from taipy.gui import notify, Markdown
from supabase import create_client, Client
import pandas as pd


def return_dados():
    tbl = None
    try:
        url: str = os.environ.get("SUPABASE_URL")
        key: str = os.environ.get("SUPABASE_KEY")
        supabase: Client = create_client(url, key)
        tbl = supabase.table("questoes").select("*").execute()
        df = pd.DataFrame(tbl.data)
        df.set_index("id", inplace=True)
    except:
        pass
    return df


# Definição de Variável
dados = return_dados()


def refresh_dados(state):
    state.dados = return_dados()


# Definição Pagina
tbl_q_md = Markdown(
    """<|container|
        
# Visualizador de Questões - Data Science

<|layout|columns=1fr|gap=5px|class_name=card|
<|c1|
<center><|Refresh|button|on_action=refresh_dados|></center>
|>
<|c3|
<|{dados}|table|page_size=2|class_name=fullwidth|>
|>
|>
|>
"""
)
