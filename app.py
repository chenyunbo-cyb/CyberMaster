import os
from flask import Flask, render_template, request
from langchain.chat_models import ChatOpenAI
import openai

app = Flask(__name__)

os.environ["OPENAI_API_KEY"] = ''

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

    return answer



if __name__ == '__main__':
    app.run(debug = True)