from langgraph.graph import StateGraph, END
from agents.state import QuizState

from agents.extractors.concept_extractor import concept_extractor
from agents.organizers.hierarchy_builder import hierarchy_builder
from agents.generators.quiz_generator import quiz_generator
from agents.rankers.difficulty_ranker import difficulty_ranker
from agents.validators.difficulty_validator import difficulty_validator


from pathlib import Path
from core.logger import get_logger

logger = get_logger(__name__)

MAX_RETRIES = 2

def validation_router(state):
    retry_count = state.get("retry_count", 0)

    if state.get("validation_passed"):
        return END

    if retry_count >= MAX_RETRIES:
        return END

    return "rank"


def build_graph(save_image: bool = True):
    """
    Builds and compiles the LangGraph.
    Optionally saves the graph image to artifacts/graphs/.
    """

    graph = StateGraph(QuizState)

    # Nodes
    graph.add_node("extract", concept_extractor)
    graph.add_node("organize", hierarchy_builder)
    graph.add_node("generate", quiz_generator)
    graph.add_node("rank", difficulty_ranker)
    graph.add_node("validate", difficulty_validator)

    # Flow
    graph.set_entry_point("extract")

    graph.add_edge("extract", "organize")
    graph.add_edge("organize", "generate")
    graph.add_edge("generate", "rank")
    graph.add_edge("rank", "validate")

    graph.add_conditional_edges(
        "validate",
        validation_router
    )

    compiled_graph = graph.compile()

    # Save graph image
    if save_image:
        try:
            artifacts_dir = Path("artifacts/graphs")
            artifacts_dir.mkdir(parents=True, exist_ok=True)

            graph_image_path = artifacts_dir / "quiz_agent_graph.png"

            compiled_graph.get_graph().draw_png(
                output_file_path=str(graph_image_path)
            )

            logger.info(
                "LangGraph image saved at %s",
                graph_image_path.resolve()
            )

        except Exception as e:
            logger.warning(
                "Failed to save LangGraph image: %s", str(e)
            )

    return compiled_graph
