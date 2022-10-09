from typing import Dict
from enum import IntEnum, unique


@unique
class Piece(IntEnum):
    EMPTY = 0
    PAWN = 1
    LANCE = 2
    KNIGHT = 3
    SILVER = 4
    GOLD = 5
    BISHOP = 6
    ROOK = 7
    KING = 8
    PROMOTED_PAWN = 9
    PROMOTED_LANCE = 10
    PROMOTED_KNGIHT = 11
    PROMOTED_SILVER = 12
    PROMOTED_BISHOP = 14
    PROMOTED_ROOK = 15
    ENEMY_PAWN = 16
    ENEMY_LANCE = 17
    ENEMY_KNIGHT = 18
    ENEMY_SILVER = 19
    ENEMY_GOLD = 20
    ENEMY_BISHOP = 21
    ENEMY_ROOK = 22
    ENEMY_KING = 23
    ENEMY_PROMOTED_PAWN = 24
    ENEMY_PROMOTED_LANCE = 25
    ENEMY_PROMOTED_KNGIHT = 26
    ENEMY_PROMOTED_SILVER = 27
    ENEMY_PROMOTED_BISHOP = 29
    ENEMY_PROMOTED_ROOK = 30


PIECE_DICT: Dict[Piece, str] = {
    Piece.PAWN: "歩",
    Piece.LANCE: "香",
    Piece.KNIGHT: "桂",
    Piece.SILVER: "銀",
    Piece.GOLD: "金",
    Piece.BISHOP: "角",
    Piece.ROOK: "飛",
    Piece.KING: "王",
    Piece.PROMOTED_PAWN: "と",
    Piece.PROMOTED_LANCE: "杏",
    Piece.PROMOTED_KNGIHT: "圭",
    Piece.PROMOTED_SILVER: "全",
    Piece.PROMOTED_BISHOP: "馬",
    Piece.PROMOTED_ROOK: "龍",
    # enemy
    Piece.ENEMY_PAWN: "歩",
    Piece.ENEMY_LANCE: "香",
    Piece.ENEMY_KNIGHT: "桂",
    Piece.ENEMY_SILVER: "銀",
    Piece.ENEMY_GOLD: "金",
    Piece.ENEMY_BISHOP: "角",
    Piece.ENEMY_ROOK: "飛",
    Piece.ENEMY_KING: "王",
    Piece.ENEMY_PROMOTED_PAWN: "と",
    Piece.ENEMY_PROMOTED_LANCE: "杏",
    Piece.ENEMY_PROMOTED_KNGIHT: "圭",
    Piece.ENEMY_PROMOTED_SILVER: "全",
    Piece.ENEMY_PROMOTED_BISHOP: "馬",
    Piece.ENEMY_PROMOTED_ROOK: "龍",
}


def is_my_piece(piece: Piece) -> bool:
    return Piece.PAWN <= piece.value <= Piece.PROMOTED_ROOK


def is_enemy_piece(piece: Piece) -> bool:
    return Piece.ENEMY_PAWN <= piece.value <= Piece.ENEMY_PROMOTED_ROOK
