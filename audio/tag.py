from enum import Enum

class TagFormat(Enum):
    INVALID = 0
    TEXT = 1
    INTEGER = 2
    FLOAT = 3
    BINARY = 4

type TagValueType = None | str | int | float | bytes

class Tag:
    
    key: str
    value: TagValueType

    @property
    def format(self) -> TagFormat:
        match self.value:
            case None:  return TagFormat.INVALID
            case str(): return TagFormat.TEXT
            case int(): return TagFormat.INTEGER
            case float(): return TagFormat.FLOAT
            case bytes(): return TagFormat.BINARY
            case _: return TagFormat.INVALID
    
    def __init__(self, key: str, value: TagValueType = None):
        self.key = key
        self.value = value
    
    def __repr__(self) -> str:
        if type(self.value) == bytes:
            return f"Tag({self.key}, {self.format}, {len(self.value)} bytes)"
        return f"Tag({self.key}, {self.format}, {self.value})"
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Tag):
            return NotImplemented
        return self.key == other.key and self.value == other.value
