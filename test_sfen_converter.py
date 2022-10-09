from piece import Piece
from sfen_converter import convert


def test_convert():
    initial_sfen = "lnsgkgsnl/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL"
    assert convert(initial_sfen).grid[0][0] == Piece.ENEMY_LANCE
