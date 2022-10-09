from typing import List
from move import Move
from piece import Piece
from dataclasses import dataclass


@dataclass
class Board:
    grid: List[List[Piece]]

    def process_move(self, move: Move):
        if move.from_row != -1 or move.from_col != -1:
            piece_type = self.grid[move.from_row][move.from_col]
            self.grid[move.from_row][move.from_col] = Piece.EMPTY
        else:
            # FIXME specify pieceType in komadai case
            piece_type = Piece.ENEMY_KING

        # TODO move piece to komadai if piece exists

        self.grid[move.to_row][move.to_col] = piece_type
