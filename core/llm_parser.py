import json
import re

class LLMParseError(Exception):
    pass

def extract_json(text):
    """
    Extracts and parses JSON from LLM output.
    Handles:
    - ```json ... ``` blocks
    - Raw JSON
    """
    if not isinstance(text, str):
        return text

    # Try fenced JSON first
    fenced = re.search(r"```json\s*(.*?)\s*```", text, re.DOTALL)
    if fenced:
        try:
            return json.loads(fenced.group(1))
        except json.JSONDecodeError as e:
            raise LLMParseError(f"Invalid fenced JSON: {e}")

    # Try raw JSON
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        raise LLMParseError("LLM did not return valid JSON")
