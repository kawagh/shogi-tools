from piece import Piece
from move import Move
from board import Board
from kif_parser import parse_move
from sfen_converter import INITIAL_SFEN, convert


def test_process_move():
    move: Move = parse_move("７六歩(77)")
    board: Board = convert(INITIAL_SFEN)
    assert board.grid[6][2] == Piece.PAWN

    board.process_move(move)

    assert board.grid[6][2] == Piece.EMPTY, "着手後に駒が残っている"
    assert board.grid[5][2] == Piece.PAWN, "着手先の駒が存在していない"


def test_process_move_updates_komadai():
    board: Board = convert(INITIAL_SFEN)
    moves = [
        parse_move("７六歩(77)"),
        parse_move("３四歩(33)"),
        parse_move("２二角成(88)"),
    ]
    for move in moves:
        board.process_move(move)
    print(board.komadai)
    assert board.komadai[Piece.BISHOP] == 1


def test_board_my_komadai():
    board: Board = convert(INITIAL_SFEN)
    moves = [
        parse_move("７六歩(77)"),
        parse_move("３四歩(33)"),
        parse_move("２二角成(88)"),
    ]
    for move in moves:
        board.process_move(move)
    assert board.my_komadai == "角"
