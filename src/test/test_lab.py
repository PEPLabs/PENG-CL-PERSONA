"""
This file will contain test cases for the automatic evaluation of your
solution in main/lab.py. You should not modify the code in this file. You should
also manually test your solution by running main/app.py.
"""
import os
import unittest

import requests

from src.main.lab import llm
from src.utilities.llm_testing_util import classify_relevancy, llm_connection_check, llm_wakeup


class TestLLMResponses(unittest.TestCase):

    """
    This function is a sanity check for the Language Learning Model (LLM) connection.
    It attempts to generate a response from the LLM. If a 'Bad Gateway' error is encountered,
    it initiates the LLM wake-up process. This function is critical for ensuring the LLM is
    operational before running tests and should not be modified without understanding the
    implications.
    Raises:
        Exception: If any error other than 'Bad Gateway' is encountered, it is raised to the caller.
    """
    def test_llm_sanity_check(self):
        try:
            response = llm_connection_check()
            self.assertIsInstance(response, LLMResult)
        except Exception as e:
            if 'Bad Gateway' in str(e):
                llm_wakeup()
                self.fail("LLM is not awake. Please try again in 3-5 minutes.")
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


if __name__ == '__main__':
    unittest.main()
