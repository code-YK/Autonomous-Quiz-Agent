from agents.validators.difficulty_validator import difficulty_validator


def test_validation_fails_for_invalid_distribution():
    fake_state = {
        "ranked_questions": [
            {"question": "Q1", "difficulty": "Hard"},
            {"question": "Q2", "difficulty": "Hard"},
            {"question": "Q3", "difficulty": "Hard"},
            {"question": "Q4", "difficulty": "Hard"},
            {"question": "Q5", "difficulty": "Hard"},
            {"question": "Q6", "difficulty": "Hard"},
            {"question": "Q7", "difficulty": "Hard"},
            {"question": "Q8", "difficulty": "Hard"},
            {"question": "Q9", "difficulty": "Hard"},
            {"question": "Q10", "difficulty": "Hard"},
        ]
    }

    result = difficulty_validator(fake_state)

    assert result["validation_passed"] is False
    assert "feedback" in result or "validation_feedback" in result