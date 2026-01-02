# agents/graph.py

from langgraph.graph import StateGraph, END
from agents.state import QuizState

from agents.extractors.concept_extractor import concept_extractor
from agents.organizers.hierarchy_builder import hierarchy_builder
from agents.generators.quiz_generator import quiz_generator
from agents.rankers.difficulty_ranker import difficulty_ranker
from agents.validators.difficulty_validator import difficulty_validator

from core.logger import get_logger

logger = get_logger(__name__)

MAX_RETRIES = 3


def validation_router(state):
    retry_count = state.get("retry_count", 0)

    if state.get("validation_passed"):
        return END

    if retry_count >= MAX_RETRIES:
        logger.error("Max validation retries reached. Accepting best effort.")
        return END

    return "rank"


def build_graph():
    """
    Builds and compiles the LangGraph.
    (Visualization handled elsewhere)
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

    graph.add_conditional_edges("validate", validation_router)

    return graph.compile()

agent = build_graph()