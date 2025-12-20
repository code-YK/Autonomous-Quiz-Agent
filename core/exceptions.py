class AgentError(Exception):
    """Base class for agent-related errors"""
    pass


class LLMInvocationError(AgentError):
    """Raised when LLM call fails"""
    pass


class ValidationError(AgentError):
    """Raised when quiz validation fails"""
    pass
