from field import Field

class Board:

    # last field distance from left edge board
    last_x_coordinate = 930
    # last field distance from left edge board
    last_y_coordinate = 930

    # initialize list of board fields with players
    def list_of_fields(self):

        # list of board fields
        list_of_fields=[]

        field=Field()
        # number which helps to move on the board
        field_number=11

        for y in range(field.start_y_coordinate,self.last_y_coordinate, field.length_of_field):

            for x in range(field.start_x_coordinate, self.last_x_coordinate, field.length_of_field):

                # fields with player 1
                if len(list_of_fields) < 16:

                    field=Field( "player_1", x, y,field_number)
                    list_of_fields.append(field)

                # empty fields
                elif len(list_of_fields) >= 16 and len(list_of_fields) < 48:

                    field=Field("empty", x, y,field_number)
                    list_of_fields.append(field)

                # fields with player 2
                else :

                    field=Field("player_2", x, y,field_number)
                    list_of_fields.append(field)
                field_number+=1

            field_number+=2

        return list_of_fields

    def delete_pawn(self,field, board):

        if board[field].player!="empty":
            board[field].player="empty"

    # to delete
    def replace_pawn(self,field, board, player_turn):

        board[field].player=player_turn

    def choosen_field(self, x, y,field_list):

        for field in field_list:
            if (field.x_coordinate <=x and field.x_end_coordinate>x and #to do: to shorten
                field.y_coordinate <=y and field.y_end_coordinate >y):

                return field_list.index(field)
    def queen_transformation(self,player,board,choosen_field):

        if player=="player_1" and board[choosen_field].field_number in [81,82,83,84,85,86,87,88]:
            board[choosen_field].player="black_queen"
        elif player=="player_2" and board[choosen_field].field_number in [11,12,13,14,15,16,17,18]:
            board[choosen_field].player="white_queen"








