from unittest import TestCase

from board import Board

class TestBoard(TestCase):

    # testing number of fields
    def test_list_of_fields(self):
        self.assertEqual(len(Board().list_of_fields()),64)


    def test_1_field_number(self):

        list=Board().list_of_fields()
        self.assertEqual(list[0].field_number,11)

    def test_2_field_number(self):

        list = Board().list_of_fields()
        self.assertEqual(list[4].field_number, 15)

    def test_3_field_number(self):
        list = Board().list_of_fields()
        self.assertEqual(list[8].field_number, 21)

    def test_4_field_number(self):
        list = Board().list_of_fields()
        self.assertEqual(list[63].field_number, 88)

    def test_5_field_number(self):
        list = Board().list_of_fields()
        self.assertEqual(list[26].field_number, 43)

    # testing number of player_1
    def test_number_of_player_1_fields(self):

        number=0
        for field in Board().list_of_fields():
            if field.player=="player_1":
                number+=1

        self.assertEqual(number,16)

    # testing number of player_2
    def test_number_of_player_2_fields(self):

        number=0
        for field in Board().list_of_fields():
            if field.player=="player_2":
                number+=1

        self.assertEqual(number,16)

    # testing number of empty fields
    def test_number_of_empty_fields(self):

        number=0
        for field in Board().list_of_fields():
            if field.player=="empty":
                number+=1

        self.assertEqual(number,32)

    # form player_1 to empty
    def  test_delete_pawn(self):

        number_of_field=1
        test_board=Board()
        list=test_board.list_of_fields()
        test_board.delete_pawn(number_of_field,list)
        self.assertEqual(list[number_of_field].player, "empty")

    # from empty to player 1
    def test_1_replace_pawn(self):
        number_of_field=20
        test_board = Board()
        list = test_board.list_of_fields()
        test_board.replace_pawn(number_of_field, list, "player_1")
        self.assertEqual(list[number_of_field].player, "player_1")

    # number of choosen field
    def test_choosen_field(self):

        x=80
        y=80
        list=Board().list_of_fields()
        number=Board().choosen_field(x,y,list)

        self.assertEqual(number,0)

    # number of last field
    def test_2_choosen_field(self):

        x=920
        y=920
        list=Board().list_of_fields()
        number=Board().choosen_field(x,y,list)

        self.assertEqual(number, 63)





