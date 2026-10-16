from dataclasses import dataclass

@dataclass
class Response:
    """ Structured response for LLM class """
    content : str = ""
    reasoning : str | None = None
    tool_call : dict | None = None
    metadata : dict | None = None

