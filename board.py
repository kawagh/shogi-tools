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


def initialize_grid() -> List[List[Piece]]:
    _grid = [[Piece.EMPTY] * 9 for _ in range(9)]

    for i in range(9):
        for j in range(9):
            if i == 0:
                if j == 0 or j == 8:
                    _grid[i][j] = Piece.ENEMY_LANCE
                if j == 1 or j == 7:
                    _grid[i][j] = Piece.ENEMY_KNIGHT
                if j == 2 or j == 6:
                    _grid[i][j] = Piece.ENEMY_SILVER
                if j == 3 or j == 5:
                    _grid[i][j] = Piece.ENEMY_GOLD
                if j == 4:
                    _grid[i][j] = Piece.ENEMY_KING
            if i == 1:
                if j == 1:
                    _grid[i][j] = Piece.ENEMY_ROOK
                if j == 7:
                    _grid[i][j] = Piece.ENEMY_BISHOP

            if i == 2:
                _grid[i][j] = Piece.ENEMY_PAWN
            if i == 6:
                _grid[i][j] = Piece.PAWN
            if i == 7:
                if j == 1:
                    _grid[i][j] = Piece.BISHOP
                if j == 7:
                    _grid[i][j] = Piece.ROOK
            if i == 8:
                if j == 0 or j == 8:
                    _grid[i][j] = Piece.LANCE
                if j == 1 or j == 7:
                    _grid[i][j] = Piece.KNIGHT
                if j == 2 or j == 6:
                    _grid[i][j] = Piece.SILVER
                if j == 3 or j == 5:
                    _grid[i][j] = Piece.GOLD
                if j == 4:
                    _grid[i][j] = Piece.KING
    return _grid
