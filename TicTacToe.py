# -*- coding: utf-8 -*-
"""
Created on Tue May 18 23:39:15 2021

@author: zeelp
"""

from IPython.display import clear_output
import random
    
def display_board(board):
    clear_output()
    print('   |   |  ')
    print(' '+board[1]+' | '+board[2]+' | '+board[3])
    print('---|---|---')
    print(' '+board[4]+' | '+board[5]+' | '+board[6])
    print('---|---|---')   
    print(' '+board[7]+' | '+board[8]+' | '+board[9])
    print('   |   |  ')
    
#test_board=['#','0','0','X','0','0','X','0','X','0']
#display_board(test_board)

def player_input():
    marker = ' '
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1 choose X or O:').upper()
    
    if marker == 'X':
        return('X','O')
    else:
        return('O','X')
    
def place_marker(board,mark,place):
    board[place] = mark
    
def check_win(board, mark):
    #win tic tak toe?
    #all row and if same marker and same for columns and diagonals too
        return ((board[1]==mark and board[2]==mark and board[3]==mark) or 
        (board[4]==mark and board[5]==mark and board[6]==mark) or
        (board[7]==mark and board[8]==mark and board[9]==mark) or
        (board[1]==mark and board[4]==mark and board[7]==mark) or
        (board[2]==mark and board[5]==mark and board[8]==mark) or
        (board[3]==mark and board[6]==mark and board[9]==mark) or
        (board[1]==mark and board[5]==mark and board[9]==mark) or
        (board[3]==mark and board[5]==mark and board[7]==mark))
    

def choose_first():
    flip = random.randint(0,1)
    
    if flip == 0:
        return 'player 1'
    else:
        return 'player 2'    
    
def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    #board is full if we return true
    return True

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose position 1 to 9:'))
    return position

def replay():
    choice = input('Play again? Enter Yes or No:')
    return choice == 'Yes'

print('WELCOME TO TIC TAC TOE')

while True:
    the_board=[' ']*10
    player1_marker,player2_marker = player_input()
    
    turn = choose_first()
    
    print(turn + ' will go first')
    
    play_game=input('Ready to play?y or n')
    
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        
        if turn == 'Player 1':
            
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)
            
            if check_win(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 has WON!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Its a TIE!!')
                    break
                else:
                    turn = 'Player 2'
            
        else:
            
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)
            
            if check_win(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 has WON!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Its a TIE!!')
                    break
                else:
                    turn = 'Player 1'
            
    
    if not replay():
        break
    
    
    
    
    
    