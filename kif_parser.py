from typing import Dict
import argparse
from pprint import pprint


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
