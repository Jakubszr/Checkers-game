from board import Board

# class to make rules to move pawns on board
class Moving:

    def __init__(self):

       pass

    # convert index to coordinate
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

    # oposite player
    def oposite_player(self,turn):
        if turn==1:
            oposite_player="player_2"
            oposite_queen="white_queen"
        elif turn==-1:
            oposite_player="player_1"
            oposite_queen = "black_queen"
        return oposite_player,oposite_queen

    def field_number(self,board,field_index):
        return board[field_index].field_number

    def choosen_number(self,board,choosen_index,player):
        return board[choosen_index].field_number
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
            oposite_queen="white_queen"
        elif turn==-1:
            oposite_player="player_1"
            oposite_queen = "black_queen"
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
                and board[coordinate_to_index[number-proper_moves[i+1]]].player in [oposite_player,oposite_queen]):

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

    # multifield queen move

    def queen_normal_move(self, field_index, choosen_index,board):

        number = board[field_index].field_number

        choosen_number = board[choosen_index].field_number

        x=choosen_number

        # to shorten
        way_of_queen=[]
        # can be done by modulo expression
        while x>=number and choosen_number%10>number%10:

            way_of_queen.append(x)
            x -= 11
            if number ==x:
                return way_of_queen

        x = choosen_number
        while x<=number and choosen_number%10<number%10:

            way_of_queen.append(x)
            x += 11
            if number ==x:
                return way_of_queen
        x = choosen_number
        while x>=number and choosen_number%10<number%10:

            way_of_queen.append(x)
            x -= 9
            if number==x:
                return way_of_queen

        x = choosen_number

        while x<=number and choosen_number%10>number%10:

            way_of_queen.append(x)
            x += 9
            if number==x:
                return way_of_queen

    def empty_way_queen_move(self,list,board):

        coordinte_to_index=self.index_to_coordinate()
        equation=True
        for i in list:
            if board[coordinte_to_index[i]].player!="empty":
                equation=False
        return equation

    def hit_move_queen(self,list,board,turn,player,queen):

        coordinte_to_index = self.index_to_coordinate()
        iterator=0
        equation = False
        oposite_player=self.oposite_player(turn)
        pawn_to_hit=0
        for i in list:

            if board[coordinte_to_index[i]].player == "empty":
                iterator+=1
            elif board[coordinte_to_index[i]].player in [player,queen]:
                iterator-=1
            elif board[coordinte_to_index[i]].player in oposite_player:
                pawn_to_hit=coordinte_to_index[i]
        if iterator==len(list)-1:
            equation=True

        return equation,pawn_to_hit

    def double_hit_queen(self,turn,choosen_index,board,player):

        oposite_player=self.oposite_player(turn)

        # number of choosen field to move
        choosen_number = board[choosen_index].field_number

        # convert coordinate number to list number
        coordinate_to_index = Moving().index_to_coordinate()

        result=False
        # fields on upper left
        x=choosen_number
        list=[]
        while  x>=0:
            x-=11
            list.append(board[self.index_to_coordinate()[x]])

        return equation