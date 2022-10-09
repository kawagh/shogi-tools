from typing import List
from piece import Piece
from dataclasses import dataclass


@dataclass
class Board:
    grid: List[List[Piece]]
