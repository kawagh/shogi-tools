from io import TextIOWrapper
from board import Board
from piece import Piece, is_enemy_piece, PIECE_DICT

SIDE_LENGTH = 40


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
