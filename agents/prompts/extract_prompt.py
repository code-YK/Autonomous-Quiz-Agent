EXTRACT_PROMPT = """
You are an educational content analyst.

From the given text:
- Extract ONLY key concepts
- Focus on definitions, principles, and important terms
- Do NOT summarize
- Return output as JSON list with:
  - name
  - description

Text:
{chunk}
"""
