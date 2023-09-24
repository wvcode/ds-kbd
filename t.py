from __future__ import print_function
import os

from apiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools

from supabase import create_client, Client
import pandas as pd

from dotenv import load_dotenv

load_dotenv()

SCOPES = "https://www.googleapis.com/auth/forms.body"
DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

# store = file.Storage("token.json")
# creds = None
# if not creds or creds.invalid:
#     flow = client.flow_from_clientsecrets("keys/client_secret_personal.json", SCOPES)
#     creds = tools.run_flow(flow, store)

# form_service = discovery.build(
#     "forms",
#     "v1",
#     http=creds.authorize(Http()),
#     discoveryServiceUrl=DISCOVERY_DOC,
#     static_discovery=False,
# )

# Request body for creating a form
NEW_FORM = {
    "info": {
        "title": "Quickstart form",
    }
}


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


# Request body to add a multiple-choice question
NEW_QUESTION = {"requests": []}

for idx, row in dados.iterrows():
    questao = row["resultado"]

    break
#     NEW_QUESTION["requests"].append(
#         {
#             "createItem": {
#                 "item": {
#                     "title": row["resultado"],
#                     "questionItem": {
#                         "question": {
#                             "required": True,
#                             "choiceQuestion": {
#                                 "type": "RADIO",
#                                 "options": [
#                                     {"value": "1965"},
#                                     {"value": "1967"},
#                                     {"value": "1969"},
#                                     {"value": "1971"},
#                                 ],
#                                 "shuffle": True,
#                             },
#                         }
#                     },
#                 },
#                 "location": {"index": idx},
#             }
#         }
#     )

# # Creates the initial form
# result = form_service.forms().create(body=NEW_FORM).execute()

# # Adds the question to the form
# question_setting = (
#     form_service.forms()
#     .batchUpdate(formId=result["formId"], body=NEW_QUESTION)
#     .execute()
# )

# # Prints the result to show the question has been added
# get_result = form_service.forms().get(formId=result["formId"]).execute()
# print(get_result)
