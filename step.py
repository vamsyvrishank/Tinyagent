from dataclasses import dataclass


@dataclass
class Step:
    """ defines a single step in agent trajectory"""
    thought : str = ""
    action : dict | None = None
    observation : str | None = None
    answer : str | None = None 
    metadata : dict | None = None
