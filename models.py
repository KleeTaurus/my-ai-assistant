from datetime import datetime
import os
import openai

openai.organization = "org-eXcqm3mDqaR6m7xWX4Z4I9gu"
openai.api_key = os.getenv("OPENAI_API_KEY")

models = openai.Model.list().data

for m in models:
    ts = int(m["created"])
    print("{0: <5}, {1: <18}, {2}, {3}".format(
        m["object"],
        m["owned_by"],
        datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'),
        m["id"]))
