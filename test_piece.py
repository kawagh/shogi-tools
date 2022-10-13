from piece import Piece, convert_piece_side, reverse_promote
import pytest


@pytest.mark.parametrize(
    "before,expected",
    [
        (Piece.PAWN, Piece.ENEMY_PAWN),
        (Piece.ENEMY_PAWN, Piece.PAWN),
    ],
)
def test_convert_piece_side(before, expected):
    assert convert_piece_side(before) == expected


def test_convert_piece_side_raise_error():
    with pytest.raises(ValueError) as e:
        convert_piece_side(Piece.EMPTY)
    assert e.type == ValueError


@pytest.mark.parametrize(
    "before,expected",
    [
        (Piece.PROMOTED_PAWN, Piece.PAWN),
        (Piece.ENEMY_PROMOTED_PAWN, Piece.ENEMY_PAWN),
    ],
)
def test_reverse_promote(before, expected):
    assert reverse_promote(before) == expected


def test_reverse_promote_raise_error():
    with pytest.raises(ValueError) as e:
        reverse_promote(Piece.PAWN)
    assert e.type == ValueError
