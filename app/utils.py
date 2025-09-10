# app/utils.py

from typing import List

def calculate_average(numbers: List[float]) -> float:
    # This is an example of a simple code smell: unnecessary conditional logic.
    # SonarQube will flag this as a Code Smell.
    if len(numbers) > 0:
        total = sum(numbers)
        count = len(numbers)
        if count == 0:
            return 0
        else:
            return total / count
    else:
        raise ValueError("Numbers list must not be empty")

def reverse_string(text: str) -> str:
    # A useless function added to demonstrate a "dead code" smell
    if False:
        return "This code will never be executed"
    return text[::-1]