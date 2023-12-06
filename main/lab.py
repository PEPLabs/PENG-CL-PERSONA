import os
import requests

"""
All requests to the LLM require some form of a key.
Other sensitive data has also been hidden through environment variables.
"""
api_key = os.environ['OPENAI_API_KEY']
base_url = os.environ['OPENAI_API_BASE']
deployment = os.environ['OPENAI_API_DEPLOYMENT']
version = os.environ['OPENAI_API_VERSION']
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
prompt = ""

"""
There is no need to change the below function. It will properly use the prompt above &
user input as needed.
"""


def llm(user_input):
    res = requests.post(f"{base_url}/deployments/{deployment}/chat/completions?api-version={version}",
                        headers={
                            "Content-Type": "application/json",
                            "api-key": f"{api_key}"
                        },
                        json={
                            "messages": [
                                {"role": "system",
                                 "content": f"{prompt}"},
                                {"role": "user",
                                 "content": f"{user_input}"}],
                        })
    message = str(res.json().get("choices")[0].get("message").get("content"))
    print(message)
    return message
