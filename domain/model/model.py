from dataclasses import dataclass

@dataclass
class Ping:
    seconds: int
    byte: int
    server: str