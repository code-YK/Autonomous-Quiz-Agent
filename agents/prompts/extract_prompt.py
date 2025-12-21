EXTRACT_PROMPT = """
You are an educational content analyst.

From the given text:
- Extract ONLY key concepts
- Focus on definitions, principles, and important terms
- summarize : 1–2 sentence intuitive explanation (student-friendly)
- Return output as JSON list with:
  - name
  - description
  - summary

Text:
{chunk}
"""
