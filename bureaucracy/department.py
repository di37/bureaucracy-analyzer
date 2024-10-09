import os, sys
from os.path import dirname as up

sys.path.append(os.path.abspath(os.path.join(up(__file__), os.pardir)))

from typing import List
from bureaucracy.constants import HR_QUESTIONS, FINANCIAL_QUESTIONS


class Department:
    def __init__(self, name: str, questions: List[str]):
        self.name = name
        self.questions = questions
        self.responses = {}

    def set_response(self, question: str, response: str):
        self.responses[question] = response

    def get_response_string(self) -> str:
        return "\n".join([f"{q}: {self.responses.get(q, '')}" for q in self.questions])


class HRDepartment(Department):
    def __init__(self):
        super().__init__("Human Resources", HR_QUESTIONS)


class FinanceDepartment(Department):
    def __init__(self):
        super().__init__("Finance", FINANCIAL_QUESTIONS)
