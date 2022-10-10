from kif_parser import KifParser
from sfen_converter import convert
from svg_board import write_svg
import subprocess
import pathlib


def main():

    initial_sfen = "lnsgkgsnl/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL"
    board = convert(initial_sfen)
    save_dir = pathlib.Path(__file__).parent / "svgs"
    save_dir.mkdir(exist_ok=True)

    with open(save_dir / "from_sfen000.svg", "w") as f:
        write_svg(f, board)

    show_svg = False

    kif_parser = KifParser("./kifs/a.kif")
    kif_parser.parse()
    for i, move in enumerate(kif_parser.moves, 1):
        print(move)
        board.process_move(move)
        save_name = save_dir / f"from_sfen{i:03}.svg"
        with open(save_name, "w") as f:
            write_svg(f, board)
        if show_svg:
            subprocess.run(["eog", save_name])


if __name__ == "__main__":
    main()
