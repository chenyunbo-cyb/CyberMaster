import os
from flask import Flask, render_template, request
from langchain.chat_models import ChatOpenAI
import openai
import requests

app = Flask(__name__)

os.environ["OPENAI_API_KEY"] = ''

# http_proxy  = "http://127.0.0.1:7890"
# https_proxy = "http://127.0.0.1:7890"
# proxies = { 
#               "http"  : http_proxy, 
#               "https" : https_proxy, 
#             }
# url = "https://api.openai.com/endpoint"

# # 设置请求头，根据需要进行定制
# headers = {
#     "Authorization": ,
#     "Content-Type": "application/json"
# }
# response = requests.get(url, headers=headers, proxies=proxies)
# # 处理响应
# print(response.text)

# First, let's load the language model we're going to use to control the agent.
chat = ChatOpenAI(temperature=0)


@app.route('/')
def hello():
    return render_template('index.html')
   
@app.route('/ask', methods=['POST'])
def ask():
    question = request.form['question']
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "请使用佛祖或大师的口吻回答"},
            {"role": "user", "content": question},
        ],
        temperature=0, # this is the degree of randomness of the model's output
    )

    answer = response.choices[0].text.strip()

    # answer = chat.ask_question(question)

    # response = "hhhh哈哈哈哈哈哈"
    # answer = response

    return answer



if __name__ == '__main__':
    app.run(debug = True)