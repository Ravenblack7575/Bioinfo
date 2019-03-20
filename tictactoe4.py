# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 06:14:25 2019
#pythonprogramming.net python3.7 basics tutorial - Making a simple TicTacToe game.
@author: RB
"""
import itertools


def win(current_game):
    
    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False
        
    #horizonal
    
    for row in game:
        print(row)
        if all_same(row):
            print(f'Player {row[0]} is the winner horizontally!')
            return True
            
    #diagonal
    
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
            print(f'Player {diags[0]} is the winner diagonally! (/)')
            return True
    
    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags):
        print(f'Player {diags[0]} is the winner diagonally! (\\)')
        return True
        
    #vertical
    for col in range(len(game)):
        check = []
        
        for row in game:
            check.append(row[col])

        if all_same(check):
            print(f'Player {check[0]} is the winner vertically!')
            return True
        
    return False
        
        
def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:    #try statement to handle for errors to begin bracketing of funct
    #parameters with defaults in the function
        if game_map[row][column] != 0:
            print('This position is occupado! Choose another!')
            return game_map, False
    
        print('  '+'  '.join([str(i) for i in range(len(game_map))]))  #top row numbers
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):  #inbuilt func enumerate
            print(count, row)
        return game_map, True
            
        
    except IndexError as e:     #if error (what type) happens do this.
        print('Error row/column input must be 0, 1 or 2', e)
        return game_map, False
    
    except Exception as e:      #any error you didn't think about.
        print('Something went very wrong!.', e)
        return game_map, False
        
    #else:    another option
    #finally: another option that is very rare
    
    
play = True
players = [1,2]
while play:
    
    game_size = int(input("What size of tic tac toe? "))
    game = [[0 for i in range(game_size)] for i in range(game_size)]
    
    game_won = False
    game, _ = game_board(game, just_display=True) #underscore means doesn't matter true or false
    player_choice = itertools.cycle([1,2])
    while not game_won:
        current_player = next(player_choice)
        print(f'Current Player: {current_player}')
        played = False
        
        while not played:
            column_choice = int(input("What column do you want to play? (0, 1, 2): "))
            row_choice = int(input("What row do you want to play? (0, 1, 2): "))
            game, played = game_board(game, current_player, row_choice, column_choice)

    
        if win(game):
            game_won = True
            again = input('The game is over. Do you want to play again? (y/n) ')
            if again.lower() == 'y':
                print('restarting...')
            elif again.lower() == 'n':
                print('byeee!')
                play = False
            else:
                print('Not a valid answer. So...c u l8r aligator.')
                play = False

