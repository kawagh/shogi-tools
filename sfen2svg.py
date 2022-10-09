from sfen_converter import convert
from svg_board import write_svg


def main():

    initial_sfen = "lnsgkgsnl/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL"
    board = convert(initial_sfen)
    with open("from_sfen.svg", "w") as f:
        write_svg(f, board)


if __name__ == "__main__":
    main()