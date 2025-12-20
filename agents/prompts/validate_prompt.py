VALIDATE_PROMPT = """
You are a strict evaluator.

Check if difficulty assignment is logical:
- Easy questions should not require scenarios
- Hard questions should require application or reasoning
- Distribution must be 3 Easy, 4 Medium, 3 Hard

Return JSON with:
- validation_passed (true/false)
- feedback

Ranked Questions:
{ranked_questions}
"""
