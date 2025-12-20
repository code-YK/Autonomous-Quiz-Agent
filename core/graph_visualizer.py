# core/graph_visualizer.py

from pathlib import Path
from core.logger import get_logger

logger = get_logger(__name__)


def save_graph_mermaid(compiled_graph, filename: str = "quiz_agent_graph.md"):
    """
    Saves LangGraph structure as a Mermaid diagram.
    No external system dependencies required.
    """

    try:
        artifacts_dir = Path("artifacts/graphs")
        artifacts_dir.mkdir(parents=True, exist_ok=True)

        graph_path = artifacts_dir / filename

        mermaid_text = compiled_graph.get_graph().draw_mermaid()

        with open(graph_path, "w", encoding="utf-8") as f:
            f.write(mermaid_text)

        logger.info("LangGraph Mermaid diagram saved at %s", graph_path.resolve())

    except Exception as e:
        logger.warning("Failed to save LangGraph Mermaid diagram: %s", str(e))
