from unittest import TestCase
from board import Board
from moving import Moving

class TestMoving(TestCase):

    def test_1_normal_move(self):

        coordinates=Moving().index_to_coordinate()


        board=Board().list_of_fields()
        turn=1

        field_number=coordinates[27] # field on pawn
        choosen_field=coordinates[38]

        Moving().normal_move(turn,field_number,choosen_field,board,"player_1")

        current_player=board[choosen_field].player
        print(board[choosen_field].player)

        self.assertEqual(current_player,"player_1")

    def test_2_normal_move(self):
        coordinates = Moving().index_to_coordinate()

        board = Board().list_of_fields()
        turn = 1

        field_number = coordinates[22]  # field on pawn
        choosen_field = coordinates[31] # choosen field

        Moving().normal_move(turn, field_number, choosen_field, board, "player_1")

        current_player = board[choosen_field].player
        print(board[choosen_field].player)

        self.assertEqual(current_player, "player_1")


    def test_3_normal_move(self):
        coordinates = Moving().index_to_coordinate()

        board = Board().list_of_fields()
        turn = -1

        field_number = coordinates[42]  # field on pawn
        choosen_field = coordinates[31] # choosen field

        Moving().normal_move(turn, field_number, choosen_field, board, "player_2")

        current_player = board[choosen_field].player
        print(board[choosen_field].player)

        self.assertEqual(current_player, "player_2")