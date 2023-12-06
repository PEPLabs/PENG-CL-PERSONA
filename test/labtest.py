"""
This file will contain test cases for the automatic evaluation of your
solution in main/lab.py. You should not modify the code in this file. You should
also manually test your solution by running main/app.py.
"""
import os
import unittest

import requests

from main.lab import llm


class TestLLMResponse(unittest.TestCase):
    """
    The agent you've defined for the lab should accept answers according to the
    listed prompt that you've provided to the agent.
    """

    def test_lab_ai_on_topic_1(self):
        question = "How do I connect my printer?"
        result = llm(question)
        classified_as_relevant_answer = classify_relevancy(result, question)
        self.assertTrue(classified_as_relevant_answer)

    def test_lab_ai_on_topic_2(self):
        question = "How do I convert my file to a pdf?"
        result = llm(question)
        classified_as_relevant_answer = classify_relevancy(result, question)
        self.assertTrue(classified_as_relevant_answer)

    """
    The persona you've defined for the lab should not accept answers that are irrelevant
    to the prompt requirements.
    """

    def test_lab_ai_off_topic_1(self):
        question = "what can you tell me about baseball?"
        result = llm(question)
        classified_as_relevant_answer = classify_relevancy(result, question)
        self.assertFalse(classified_as_relevant_answer)

    def test_lab_ai_off_topic_2(self):
        question = "How do I make carbonara pasta?"
        result = llm(question)
        classified_as_relevant_answer = classify_relevancy(result, question)
        self.assertFalse(classified_as_relevant_answer)


"""
Function used for evaluating the LLM's own responses within tests. Not a test.
"""


def classify_relevancy(message, question):
    api_key = os.environ['OPENAI_API_KEY']
    base_url = os.environ['OPENAI_API_BASE']
    deployment = os.environ['OPENAI_API_DEPLOYMENT']
    version = os.environ['OPENAI_API_VERSION']
    deployment = os.environ['DEPLOYMENT_NAME']
    prompt = (f"Answer the following quest with a 'Yes' or 'No' response. Does the"
              f"message below successfully answer the following question?"
              f"message: {message}"
              f"question: {question}")
    res = requests.post(f"{base_url}/deployments/{deployment}/chat/completions?api-version={version}",
                        headers={
                            "Content-Type": "application/json",
                            "api-key": f"{api_key}"
                        },
                        json={
                            "messages": [
                                {"role": "user",
                                 "content": f"{prompt}"},
                                ],
                        })
    message = str(res.json().get("choices")[0].get("message").get("content"))

    if ("yes" in message.lower()):
        return True
    else:
        return False


if __name__ == '__main__':
    unittest.main()
