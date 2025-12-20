QUIZ_PROMPT = """
You are an exam paper setter.

Using the given hierarchy:
- Generate EXACTLY 10 questions
- Mix factual, conceptual, and application-based questions
- Each question must include:
  - question
  - related_concept

Return JSON list only.

Hierarchy:
{hierarchy}
"""
