import os
import openai
openai.organization = "org-eXcqm3mDqaR6m7xWX4Z4I9gu"
openai.api_key = os.getenv("OPENAI_API_KEY")
print(openai.Model.list())
