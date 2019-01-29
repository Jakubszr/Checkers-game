import pygame
import sys

from pygame.locals import *
from board import Board
from moving import Moving

pygame.init()
win = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()
pygame.mouse.set_visible(0)

# name of app in the left upper corner
pygame.display.set_caption("Checkers")

# backscreen, pawns and other graphics
bg=pygame.transform.scale(pygame.image.load('board.jpg'), (1000,1000))
player_1=pygame.transform.scale(pygame.image.load('black_pawn.png'), (100,100))
player_2=pygame.transform.scale(pygame.image.load('white_pawn.png'), (100,100))
choosen=pygame.transform.scale(pygame.image.load('yellow_pawn.png'), (100,100))

# show mouse indicator
pygame.mouse.set_visible(True)

# initiate board with players pawns
field_list=Board().list_of_fields()

# variables to define turns
player_turn=1
number = -1
run=True
multihit=False

# mouse field chose
mouse_events_list=[]

# game loop
while run:

    # collect only mouse click
    pygame.event.set_blocked(pygame.MOUSEMOTION)

    clock.tick(60)
    win.blit(bg, (0, 0))

    # display pawns depending of status
    for field in field_list:

        if field.player== "player_1":
            win.blit(player_1, (field.x_coordinate, field.y_coordinate))
        elif field.player== "player_2":
            win.blit(player_2, (field.x_coordinate,field.y_coordinate))
        elif field.player == "choosen":
            win.blit(choosen, (field.x_coordinate, field.y_coordinate))

    # get mouse coordiantes
    x, y = pygame.mouse.get_pos()

    # loop after mouse action
    for event in pygame.event.get():

        # change player depending on turn
        if player_turn==1:
            player="player_1"
        else:
            player="player_2"

        # convert mouse coordinates to index of board list
        choosen_field = Board().choosen_field(x, y, field_list)
        # closing game
        if event.type == pygame.QUIT:
            sys.exit()
        # actions after click on the pawns
        if event.type == pygame.MOUSEBUTTONDOWN:
            if field_list[choosen_field].player==player and multihit==False:
                loop_no = 0

                if multihit==False:
                    field_list[choosen_field].player="choosen"

                mouse_events_list.append(choosen_field)
                print("mouse event",mouse_events_list)
                # to do write the method
                #
                if len(mouse_events_list) >= 1:
                    one_click_before = mouse_events_list[len(mouse_events_list) - 1]
                if len(mouse_events_list) >= 2:
                    two_click_before = mouse_events_list[len(mouse_events_list) - 2]

                # change of selected pawn

                if (len(mouse_events_list) >=2 and field_list[two_click_before].player=="choosen"
                    and multihit==False):

                    field_list[mouse_events_list[len(mouse_events_list) - 2]].player = player

            #elif field_list[choosen_field].player=="empty" and multihit==True:
             #   mouse_events_list.append(choosen_field)

            # choice of field to move the pawn
            elif field_list[choosen_field].player=="empty":
                # move the pawn to allowed
                try:
                    if Moving().normal_move(player_turn, one_click_before, # to do: to shorten
                                         choosen_field,field_list,player)\
                                        and multihit==False:
                        # clear field of moved pawn
                        Board().delete_pawn(one_click_before,field_list)

                        player_turn*=-1
                except:
                    pass
                #hitting move
                try:
                    if Moving().hit_move(player_turn,one_click_before,choosen_field,field_list,player):

                        Board().delete_pawn(one_click_before, field_list)

                        if Moving().double_hit_check(choosen_field,field_list,player)==True:
                            field_list[choosen_field].player = "choosen"
                            player_turn*=-1
                            mouse_events_list.append(choosen_field)
                            one_click_before=choosen_field
                            print(mouse_events_list)
                            multihit=True
                        else:
                            multihit=False


                        player_turn*=-1

                except:
                    pass
    # update the screen
    pygame.display.update()

if __name__ == '__main__':
    main()