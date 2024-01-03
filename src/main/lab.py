import os
import requests

from langchain_community.chat_models.huggingface import ChatHuggingFace
from langchain.llms import HuggingFaceEndpoint
from langchain.schema import (
    HumanMessage,
    SystemMessage,
)

"""
The function at the bottom of the file will use the string defined below to form a 
system prompt. Then, user input will be sent to the LLM. In this case, we would 
like to create a custom chat bot for our business's need, with a tech support. 
Because we may add this to a public-facing site, we'd like to restrict the 
capabilities of the site chatbot, and limit it to discussing only tech-support 
related queries, such as "how do i convert a file to pdf?". Test cases will verify
that the app accepts tech-support queries, and rejects all other queries.
"""

"""
TODO: Change the prompt below to create a persona for the LLM as described above.
"""
prompt = "You are a tech support specialist. Only answer questions that relate to tech support. All other questions should be politely declined and the question should not be answered."

"""
There is no need to change the below function. It will properly use the prompt above &
user input as needed.
"""


def llm(user_input):
    llm = HuggingFaceEndpoint(
        endpoint_url=os.environ['LLM_ENDPOINT'],
        task="text2text-generation",
        model_kwargs={
            "max_new_tokens": 200
        }
    )
    chat_model = ChatHuggingFace(llm=llm)

    messages = [
        SystemMessage(content = prompt),
        HumanMessage(content = user_input)
    ]

    message = chat_model.invoke(messages)

    return message.content
