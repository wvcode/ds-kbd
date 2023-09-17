# -*- coding: utf-8 -*-
import os
from taipy.gui import Gui, notify
from dotenv import load_dotenv

load_dotenv()

from pages.gen_quest import gen_q_md
from pages.tbl_quest import tbl_q_md
from pages.sum_quest import sum_q_md

pages = {
    "/": "<center><|navbar|></center>",
    "Gerar": gen_q_md,
    "Visualizar": tbl_q_md,
    "Sumario": sum_q_md,
}


# ----------------------------------------------------------------
# Main
# ----------------------------------------------------------------
if __name__ == "__main__":
    Gui(pages=pages).run(
        title="WVCode - Gerador de Questões de Ciência de Dados",
        host="0.0.0.0",
        port=os.getenv("PORT"),
        use_reloader=True,
    )
