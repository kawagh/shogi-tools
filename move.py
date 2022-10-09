from dataclasses import dataclass


@dataclass
class Move:
    from_row: int
    from_col: int
    to_row: int
    to_col: int
    promote: bool = False
