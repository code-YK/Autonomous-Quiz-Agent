from agents.graph import build_graph

def run_quiz_agent(raw_text: str):
    try:
        graph = build_graph()
        return graph.invoke({"raw_text": raw_text})

    except Exception as e:
        import traceback
        traceback.print_exc()
        raise
