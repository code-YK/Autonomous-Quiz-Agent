HIERARCHY_PROMPT = """
You are a curriculum designer.

Using the given list of concepts:
- Organize them into a hierarchical structure:
  Topic → Subtopic → Concepts
- Avoid duplication
- Return valid JSON only

Concepts:
{concepts}
"""
