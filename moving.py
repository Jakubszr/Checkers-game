from board import Board

# class to make rules to move pawns on board
class Moving:

    def __init__(self):

       pass

    def index_to_coordinate(self):
        # dictionary to transform index to coordinate of field
        index_to_coordinate={}
        # coordinate of field, rule: counting from upper left corner
        # number is assign as the row and column number
        # for example: first field: 1 row and 1 column is equal 11
        coordinate=11
        # index of field in list containing objects of fields
        index=0
        # loop to connect index with coordinate of field
        for i in range(0,8):

            for j in range(0,8):
                index_to_coordinate[coordinate]=index
                coordinate+=1
                index+=1

            coordinate+=2

        return index_to_coordinate

    # normal move wihout clashing the pawn
    def normal_move(self,turn,field_index,choosen_index,board,player):

        number = board[field_index].field_number

        choosen_number = board[choosen_index].field_number

        if number+turn*9==choosen_number and board[choosen_index].player=="empty":

            Board().replace_pawn(choosen_index,board,player)

            return True

        elif number+turn*11==choosen_number and board[choosen_index].player=="empty":

            Board().replace_pawn(choosen_index,board, player)

            return True

    # move with clashing the pawn
    def hit_move(self,turn,field_index,choosen_index,board,player):

        # create oposite player to if statement
        if turn==1:
            oposite_player="player_2"
        elif turn==-1:
            oposite_player="player_1"

        # number of field - coordinate
        number = board[field_index].field_number

        # number of choosen field to move
        choosen_number = board[choosen_index].field_number

        # convert coordinate number to list number
        coordinate_to_index=Moving().index_to_coordinate()

        proper_moves=[-18,-9,-22,-11,+18,+9,+22,+11]

        for i in range(0,len(proper_moves),2):
            try:
                if (choosen_number==number-proper_moves[i] and board[choosen_index].player=="empty"
                and board[coordinate_to_index[number-proper_moves[i+1]]].player==oposite_player):

                    Board().replace_pawn(choosen_index, board, player)
                    Board().delete_pawn(coordinate_to_index[number-proper_moves[i+1]],board)

                    return True
            except KeyError:
                pass


    def double_hit_check(self,choosen_index,board,player):
        # create oposite player to if statement
        if player == "player_1":
            oposite_player = "player_2"
        elif player == "player_2":
            oposite_player = "player_1"


        # number of choosen field to move
        choosen_number = board[choosen_index].field_number

        # convert coordinate number to list number
        coordinate_to_index = Moving().index_to_coordinate()

        proper_moves = [-18, -9, -22, -11, +18, +9, +22, +11]
        equation=False
        for i in range(0, len(proper_moves), 2):
            try:
                if (board[coordinate_to_index[choosen_number+proper_moves[i]]].player=="empty"
                        and board[coordinate_to_index[choosen_number+proper_moves[i+1]]].player==oposite_player):

                    equation=True

            except KeyError:
                pass
        return equation

    def multihit_move(self):
        pass
    # multifield queen move
    def queen_move(self):
        pass