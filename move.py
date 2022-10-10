from dataclasses import dataclass


@dataclass
class Move:
    """
    if from_row = -1, the move is from komadai and from_col encodes piece type
    """

    from_row: int
    from_col: int
    to_row: int
    to_col: int
    promote: bool = False

    def is_from_komadai(self) -> bool:
        return self.from_row == -1
