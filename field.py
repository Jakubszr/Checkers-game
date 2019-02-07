class Field:

    # first field distance from left edge board
    start_x_coordinate=62

    # length of field
    length_of_field=110

    # first field distance from upper edge board
    start_y_coordinate=62

    def __init__ (self,player="empty",x_coordinate=start_x_coordinate,y_coordinate=start_y_coordinate,field_number=11):

        self.player=player
        self.x_coordinate=x_coordinate
        self.x_end_coordinate=x_coordinate+self.length_of_field
        self.y_coordinate=y_coordinate
        self.y_end_coordinate=y_coordinate+self.length_of_field
        self.field_number=field_number
