from typing import Dict
import argparse
from pprint import pprint
from dataclasses import dataclass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        "--file",
        required=True,
        help=".kif file path to parse",
    )
    args = parser.parse_args()
    return args


@dataclass
class Move:
    from_row: int
    from_col: int
    to_row: int
    to_col: int
    promote: bool = False


def parse_move(move: str) -> Move:
    """
    example
    ６六銀(77)
    ８四角打
    """
    dan = "一二三四五六七八九"
    suji = "１２３４５６７８９"
    if "打" in move:
        from_row = -1
        from_col = -1
    else:
        from_row = int(move[-3]) - 1
        from_col = 9 - int(move[-2])  # 1-index
    to_row = dan.index(move[1])
    to_col = 8 - suji.index(move[0])  # 0-index

    return Move(from_row, from_col, to_row, to_col, move.endswith("成"))


def main():
    """parse .kif file"""
    args = parse_args()
    kif_info: Dict[str, str] = {}
    with open(args.file, "r") as f:
        separator = "："
        kif_started = False
        while line := f.readline().rstrip():
            if line[:2] == "手数":
                kif_started = True
                continue
            if kif_started:
                move_info = list(filter(None, line.split(" ")))  # remove spaces
                if len(move_info) == 1:
                    print("備考", move_info)
                elif len(move_info) == 2:
                    print(move_info[-1])  # ex. 投了
                elif len(move_info) == 3:
                    move_index, move, time = move_info
                    print(move_index, move, time)
                else:
                    raise RuntimeError("unexpected")
            else:
                # parse info
                index = line.find(separator)
                if index != -1:
                    key = line[:index]
                    value = line[index + 1 :]
                    print(key, value)
                    kif_info[key] = value
    pprint(kif_info)


if __name__ == "__main__":
    main()
