from piece import Piece
from kif_parser import Move, parse_move


def test_parse_move():
    move = "６六銀(77)"
    parsed_move = parse_move(move)
    assert parsed_move == Move(from_row=6, from_col=2, to_row=5, to_col=3)


def test_parse_move_from_komadai():
    move = "８四角打"
    parsed_move = parse_move(move)
    assert parsed_move == Move(
        from_row=-1, from_col=Piece.BISHOP.value, to_row=3, to_col=1
    )
