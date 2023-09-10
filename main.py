# -*- coding: utf-8 -*-
import os
from taipy.gui import Gui, notify
from dotenv import load_dotenv

load_dotenv()

from pages.gen_quest import gen_q_md
from pages.tbl_quest import tbl_q_md

pages = {
    "/": "<center><|navbar|></center>",
    "Gerar": gen_q_md,
    "Visualizar": tbl_q_md,
}


# ----------------------------------------------------------------
# Main
# ----------------------------------------------------------------
if __name__ == "__main__":
    Gui(pages=pages).run(host="0.0.0.0", port=os.getenv("PORT"), use_reloader=True)
