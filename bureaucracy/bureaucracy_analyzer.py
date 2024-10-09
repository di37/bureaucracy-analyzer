import os, sys
from os.path import dirname as up

sys.path.append(os.path.abspath(os.path.join(up(__file__), os.pardir)))

import google.generativeai as genai

from bureaucracy.department import Department, HRDepartment
from bureaucracy.constants import (
    HR_EXAMPLE,
    FINANCE_EXAMPLE,
    GEMINI_API_KEY,
    MODEL_NAME,
)

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)


class BureaucracyAnalyzer:
    def __init__(self):
        self.model = genai.GenerativeModel(MODEL_NAME)

    def analyze_stream(self, department: Department) -> str:

        example = (
            HR_EXAMPLE if isinstance(department, HRDepartment) else FINANCE_EXAMPLE
        )

        prompt = f"""You are an AI assistant specialized in analyzing and reducing bureaucracy in various departments. Your task is to analyze responses from different departments, identify bottlenecks, calculate bureaucracy levels, propose actions to reduce bureaucracy, and estimate improvements. Use the provided examples as a guide for your analysis and recommendations.

        {example}

        Now, analyze the responses provided by the {department.name} Department below:

        {department.get_response_string()}

        1. Identify bottlenecks and pain points contributing to bureaucracy.
        2. Calculate the bureaucracy level based on the responses, assigning points to reflect issues like approval levels, manual processes, delays, and interdepartmental coordination.
        3. Propose specific actions to reduce bureaucracy. Provide examples for each proposed action.
        4. Calculate the expected bureaucracy score after implementing the suggested actions.
        5. Provide a summary of expected improvements, including the reduction percentage.

        Key points to consider in your analysis:

        - Assign scores to quantify the level of bureaucracy (e.g., number of approval levels, time delays, frequency of manual processes).
        - Identify specific bottlenecks for each question and propose relevant actions.
        - Suggest tools and technologies to simplify identified issues.
        - Calculate before and after bureaucracy scores to demonstrate the impact of your solutions.

        Final Output: Provide a clear and concise summary of the identified bottlenecks, proposed actions, expected improvements, and the calculated reduction in bureaucracy levels for the department.
        """
        return self.model.generate_content(prompt, stream=True)
