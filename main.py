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

# mouse field chose
mouse_events_list=[]

# game loop
while run:
    # to do: consider delete turn
    if number % 2 == 1:
        turn = True
    else:
        turn = False
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
            player_turn="player_2"

        # convert mouse coordinates to index of board list
        choosen_field = Board().choosen_field(x, y, field_list)

        # closing game
        if event.type == pygame.QUIT:
            sys.exit()
        # actions after click on the pawns
        if event.type == pygame.MOUSEBUTTONDOWN:
            # choice of pawn to move
            if turn==True and field_list[choosen_field].player=="player_1":
                loop_no = 0

                field_list[choosen_field].player="choosen"

                mouse_events_list.append(choosen_field)
                # change of selectted pawn
                if (len(mouse_events_list) >=2 and
                        field_list[mouse_events_list[len(mouse_events_list)-2]].player=="choosen"):

                    field_list[mouse_events_list[len(mouse_events_list) - 2]].player = player

                #number += 1
                position_in_field=loop_no

                loop_no+=1
            # choice of field to move the pawn
            elif turn==True and  player_turn==1 and field_list[choosen_field].player=="empty":
                # move the pawn to allowed
                if Moving().normal_move(player_turn, mouse_events_list[len(mouse_events_list)-1], # to do: to shorten
                                     choosen_field,field_list,player)==True:
                    # clear field of moved pawn
                    field_list[mouse_events_list[len(mouse_events_list)-1]].player = "empty" # to do: use the method

    # update the screen
    pygame.display.update()

if __name__ == '__main__':
    main()