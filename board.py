from collections import defaultdict
from typing import DefaultDict, List, Optional
from move import Move
from piece import (
    Piece,
    convert_piece_side,
    is_promoted_piece,
    reverse_promote,
)
from dataclasses import dataclass, field


@dataclass
class Board:
    grid: List[List[Piece]]
    last_move: Optional[Move] = None
    komadai: DefaultDict[Piece, int] = field(default_factory=lambda: defaultdict(int))

    def process_move(self, move: Move):
        self.last_move = move
        if move.from_row != -1 or move.from_col != -1:
            piece_type = self.grid[move.from_row][move.from_col]
            self.grid[move.from_row][move.from_col] = Piece.EMPTY
        else:
            # FIXME specify pieceType in komadai case
            piece_type = Piece.ENEMY_KING

        # move piece to komadai if piece exists
        removed_piece = self.grid[move.to_row][move.to_col]
        if removed_piece != Piece.EMPTY:
            if is_promoted_piece(removed_piece):
                removed_piece = reverse_promote(removed_piece)
            converted_removed_piece = convert_piece_side(removed_piece)
            self.komadai[converted_removed_piece] += 1

        self.grid[move.to_row][move.to_col] = piece_type
