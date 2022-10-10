from io import TextIOWrapper
from board import Board, initialize_grid
from piece import is_enemy_piece, PIECE_DICT

SIDE_LENGTH = 40


def write_svg(f: TextIOWrapper, board: Board):
    header = '<svg width="400" height="400" xmlns="http://www.w3.org/2000/svg">'
    f.write(header)

    write_content(f, board)

    footer = "</svg>"
    f.write(footer)


def write_content(f: TextIOWrapper, board: Board):
    for i in range(9):
        for j in range(9):
            is_last_move: bool = (
                board.last_move is not None
                and board.last_move.to_row == i
                and board.last_move.to_col == j
            )
            fill_color = "yellow" if is_last_move else "white"

            content = f'<rect width="{SIDE_LENGTH}" height="{SIDE_LENGTH}" x="{10+j*SIDE_LENGTH}" y="{10+i*SIDE_LENGTH}" fill="{fill_color}" stroke="gray" />\n'
            f.write(content)

            if board.grid[i][j] in PIECE_DICT:
                write_piece(
                    f,
                    PIECE_DICT[board.grid[i][j]],
                    i,
                    j,
                    is_enemy_piece(board.grid[i][j]),
                    is_last_move,
                )


def write_piece(
    f: TextIOWrapper,
    char: str,
    row: int,
    col: int,
    rotate: bool = False,
    last_move: bool = False,
):
    style = 'style="font-weight:bold;"' if last_move else ""
    rotate_transform = (
        f'transform="rotate(180,{10+col*SIDE_LENGTH+SIDE_LENGTH//2},{10+SIDE_LENGTH//2+row*SIDE_LENGTH})"'
        if rotate
        else ""
    )
    content = f'<text x="{10+col*SIDE_LENGTH}" y="{10+SIDE_LENGTH+row*SIDE_LENGTH-5}" font-size="40" {rotate_transform} {style}> {char} </text>'
    f.write(content)


def main():
    board = Board(grid=initialize_grid())
    with open("board.svg", "w") as f:
        write_svg(f, board)


if __name__ == "__main__":
    main()
