VALIDATE_PROMPT = """
You are a strict JSON validator.

Rules:
- Easy questions: simple recall
- Medium questions: conceptual understanding
- Hard questions: reasoning or application

INPUT:
{ranked_questions}

You MUST respond in valid JSON ONLY.

Schema:
{{
  "valid": true | false,
  "reason": "<short explanation>"
}}

No markdown.
No extra text.
Only JSON.
"""
