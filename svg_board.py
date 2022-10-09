from io import TextIOWrapper

SIDE_LENGTH = 40


def write_svg(f: TextIOWrapper):
    header = '<svg width="400" height="400" xmlns="http://www.w3.org/2000/svg">'
    f.write(header)

    write_content(f)

    footer = "</svg>"
    f.write(footer)


def write_content(f: TextIOWrapper):
    for i in range(9):
        for j in range(9):
            content = f'<rect width="{SIDE_LENGTH}" height="{SIDE_LENGTH}" x="{10+j*SIDE_LENGTH}" y="{10+i*SIDE_LENGTH}" fill="white" stroke="gray" />\n'
            f.write(content)

            if i == 6:
                write_piece(f, "歩", i, j)
            if i == 7 and j == 1:
                write_piece(f, "角", i, j)
            if i == 7 and j == 7:
                write_piece(f, "飛", i, j)
                print(i)
            if i == 8:
                if j == 0 or j == 8:
                    write_piece(f, "香", i, j)
                if j == 1 or j == 7:
                    write_piece(f, "桂", i, j)
                if j == 2 or j == 6:
                    write_piece(f, "銀", i, j)
                if j == 3 or j == 5:
                    write_piece(f, "金", i, j)
                if j == 4:
                    write_piece(f, "王", i, j)


def write_piece(f: TextIOWrapper, char: str, row: int, col: int):
    content = f'<text x="{10+col*SIDE_LENGTH}" y="{10+SIDE_LENGTH+row*SIDE_LENGTH-5}" font-size="40"> {char} </text>'
    f.write(content)


def main():
    with open("out.svg", "w") as f:
        write_svg(f)


if __name__ == "__main__":
    main()
