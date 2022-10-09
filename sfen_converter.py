from typing import Dict, List
from board import Board
from piece import Piece


INITIAL_SFEN = "lnsgkgsnl/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL"

SFEN_DICT: Dict[str, Piece] = {
    "l": Piece.ENEMY_LANCE,
    "n": Piece.ENEMY_KNIGHT,
    "s": Piece.ENEMY_SILVER,
    "g": Piece.ENEMY_GOLD,
    "k": Piece.ENEMY_KING,
    "r": Piece.ENEMY_ROOK,
    "b": Piece.ENEMY_BISHOP,
    "p": Piece.ENEMY_PAWN,
    # my side
    "L": Piece.LANCE,
    "N": Piece.KNIGHT,
    "S": Piece.SILVER,
    "G": Piece.GOLD,
    "K": Piece.KING,
    "R": Piece.ROOK,
    "B": Piece.BISHOP,
    "P": Piece.PAWN,
}


def convert(sfen: str) -> Board:
    _grid: List[List[Piece]] = [[Piece.EMPTY] * 9 for _ in range(9)]
    for i, line in enumerate(sfen.split("/")):
        col = 0
        for c in line:
            if c.isdigit():
                col += int(c)
            else:
                _grid[i][col] = SFEN_DICT[c]
                col += 1
        assert col == 9

    return Board(_grid)
