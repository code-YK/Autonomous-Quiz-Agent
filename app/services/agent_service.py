from agents.graph import build_graph
from core.graph_visualizer import save_graph_mermaid


def run_quiz_agent(raw_text: str, save_graph: bool = True):
    try:
        graph = build_graph()

        if save_graph:
            save_graph_mermaid(graph)

        return graph.invoke({"raw_text": raw_text})

    except Exception as e:
        import traceback
        traceback.print_exc()
        raise
