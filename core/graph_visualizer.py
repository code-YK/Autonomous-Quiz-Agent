# core/graph_visualizer.py
from pathlib import Path
from core.logger import get_logger

logger = get_logger(__name__)

from agents.graph import build_graph
from pathlib import Path

def save_graph_png():
    graph = build_graph()

    # Get Mermaid-rendered PNG bytes
    png_bytes = graph.get_graph().draw_mermaid_png()

    # Output path
    out_dir = Path("artifacts/graphs")
    out_dir.mkdir(parents=True, exist_ok=True)

    out_path = out_dir / "quiz_agent_graph.png"

    with open(out_path, "wb") as f:
        f.write(png_bytes)

    print(f"Graph image saved at: {out_path.resolve()}")

if __name__ == "__main__":
    save_graph_png()
