from io import TextIOWrapper
from typing import Dict, List
from dataclasses import dataclass
from enum import IntEnum, unique

SIDE_LENGTH = 40


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


@dataclass
class Board:
    grid: List[List[Piece]]


def initialize_grid():
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


def write_svg(f: TextIOWrapper, board: Board):
    header = '<svg width="400" height="400" xmlns="http://www.w3.org/2000/svg">'
    f.write(header)

    write_content(f, board)

    footer = "</svg>"
    f.write(footer)


def write_content(f: TextIOWrapper, board: Board):
    for i in range(9):
        for j in range(9):
            content = f'<rect width="{SIDE_LENGTH}" height="{SIDE_LENGTH}" x="{10+j*SIDE_LENGTH}" y="{10+i*SIDE_LENGTH}" fill="white" stroke="gray" />\n'
            f.write(content)

            if board.grid[i][j] in PIECE_DICT:
                write_piece(
                    f,
                    PIECE_DICT[board.grid[i][j]],
                    i,
                    j,
                    is_enemy_piece(board.grid[i][j]),
                )


def write_piece(f: TextIOWrapper, char: str, row: int, col: int, rotate: bool = False):
    if rotate:
        content = f'<text x="{10+col*SIDE_LENGTH}" y="{10+SIDE_LENGTH+row*SIDE_LENGTH-5}" font-size="40" transform="rotate(180,{10+col*SIDE_LENGTH+SIDE_LENGTH//2},{10+SIDE_LENGTH//2+row*SIDE_LENGTH})"> {char} </text>'
    else:
        content = f'<text x="{10+col*SIDE_LENGTH}" y="{10+SIDE_LENGTH+row*SIDE_LENGTH-5}" font-size="40"> {char} </text>'
    f.write(content)


def main():
    board = Board(grid=initialize_grid())
    with open("board.svg", "w") as f:
        write_svg(f, board)


if __name__ == "__main__":
    main()
