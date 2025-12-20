RANK_PROMPT = """
You are an assessment expert.

Assign difficulty to each question:
- Easy: definition, direct recall
- Medium: explanation, comparison
- Hard: application, scenario-based

Return JSON list with:
- question
- difficulty (Easy | Medium | Hard)

Questions:
{questions}
"""
