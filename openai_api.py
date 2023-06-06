#!/bin/env python
#coding=utf-8

import os
import openai
import time
# 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  
# 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
# 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
# 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
# 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
OPENAI_API_KEY = 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

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_completions(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=0,
            )
    return response.choices[0].message["content"]

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=temperature,
            )
    time.sleep(20)
    return response.choices[0].message["content"]