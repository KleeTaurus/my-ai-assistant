import os
import openai

openai.organization = "org-eXcqm3mDqaR6m7xWX4Z4I9gu"
openai.api_key = os.getenv("OPENAI_API_KEY")

# https://www.zhihu.com/question/21832379/answer/19492362
# 如果你是《了不起的盖茨比》中的盖茨比，且深爱着黛西，会如何优雅地追回她？

the_question = """
提供下 vscode 最常用的20个快捷键
"""

response = openai.Completion.create(
    model="text-davinci-003",
    prompt=the_question,
    max_tokens=2048,
    temperature=1,
)

print("Your question: \n{}".format(the_question))
print("OpenAI answer: \n{}".format(response.choices[0].text))
