from agents.graph import build_graph

def test_agent_graph_execution(sample_text):
    graph = build_graph(save_image=False)

    result = graph.invoke({
        "raw_text": sample_text
    })

    # Core outputs exist
    assert "concepts" in result
    assert "hierarchy" in result
    assert "questions" in result
    assert "ranked_questions" in result

    assert isinstance(result["ranked_questions"], list)
    assert len(result["ranked_questions"]) == 10

    # Validation outcome is deterministic
    assert "validation_passed" in result
    assert isinstance(result["validation_passed"], bool)
