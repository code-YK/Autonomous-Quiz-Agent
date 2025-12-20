import pytest
from unittest.mock import patch


@pytest.fixture
def sample_text():
    return """
    Machine Learning is a field of Artificial Intelligence.
    Overfitting occurs when a model learns noise.
    Underfitting happens when a model is too simple.
    Bias-Variance Tradeoff explains model generalization.
    """


@pytest.fixture(autouse=True)
def mock_llm():
    """
    Mock invoke_llm everywhere it is USED.
    """
    patches = [
        "agents.extractors.concept_extractor.invoke_llm",
        "agents.organizers.hierarchy_builder.invoke_llm",
        "agents.generators.quiz_generator.invoke_llm",
        "agents.rankers.difficulty_ranker.invoke_llm",
        "agents.validators.difficulty_validator.invoke_llm",
    ]

    with ExitStack() as stack:
        for target in patches:
            mock = stack.enter_context(patch(target))
            mock.side_effect = fake_llm_response
        yield


from contextlib import ExitStack


def fake_llm_response(prompt: str):
    if "Extract ONLY key concepts" in prompt:
        return [
            {"name": "Overfitting", "description": "Model learns noise"},
            {"name": "Underfitting", "description": "Model too simple"},
        ]

    if "hierarchical structure" in prompt:
        return {
            "Machine Learning": {
                "Model Evaluation": ["Overfitting", "Underfitting"]
            }
        }

    if "Generate EXACTLY 10 questions" in prompt:
        return [
            {"question": f"Question {i}", "related_concept": "Overfitting"}
            for i in range(1, 11)
        ]

    if "Assign difficulty" in prompt:
        return [
            {"question": f"Question {i}", "difficulty": d}
            for i, d in enumerate(
                ["Easy"] * 3 + ["Medium"] * 4 + ["Hard"] * 3, start=1
            )
        ]

    if "strict evaluator" in prompt:
        return {
            "validation_passed": False,
            "feedback": "Invalid difficulty distribution"
        }

    return {}
