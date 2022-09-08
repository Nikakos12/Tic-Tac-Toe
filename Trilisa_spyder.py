# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 11:47:17 2022

@author: WINDOWS10
"""

def names_request():
    
    global player_1
    global player_2
    
    player_1 = input('Player_1 please type your name: \n')
    player_2 = input('Player_1 please type your name: \n')
    
    return player_1,player_2

# function that asks for the players to type their perferance for where to put their x or o:

def location_request():
    
    global num_position
    global name
    global text
    
    text = ''
    
    if i%2==0:
        name = player_2
        text= p2_choice
    else:
        text = p1_choice
        name = player_1
    
    print(f"{name} it's your turn to play")
    
    answer = False
    while answer == False:
        
        #asking for position
        position = input("Please choose a position between 1 to 9 and hit the 'Enter' button : ")
        
        #check if the position is a positive and integer number                 
        if position.isdigit():
            num_position = int(position)
            #check if the number is within the 1 to 9 space
            if num_position not in [1,2,3,4,5,6,7,8,9]:
                pass
            else:
                answer == True
                return num_position
        else:
            pass
        
#function that gives the users the opportunity to keep playing or leave the game
def exit_plan():
    
    global leave
    global choices
    global i
    
    answer = False
    
    while answer == False:
        
        valid = input("Please type 'Y' to keep playing or 'N' to exit ")
        
        if valid.upper() == 'Y':
            choices = [1,2,3,4,5,6,7,8,9]
            i=0
            return'Thank you for keep playing...'
        
        elif valid.upper() == 'N':
            print('Thank you for playing have a nice day...!')
            leave = True
            answer = True
            
        else:
            pass   
        
def display_runner():
     
    print(f"   |   |   ")
    print(f" {choices[0]} | {choices[1]} | {choices[2]} ")  #row_1
    print(f"___|___|___")
    print(f"   |   |   ")
    print(f" {choices[3]} | {choices[4]} | {choices[5]} ")  #row_2
    print(f"___|___|___")
    print(f"   |   |   ")
    print(f" {choices[6]} | {choices[7]} | {choices[8]} ")  #row_3
    print(f"   |   |   ")
    
    return choices

# this function gives the user the chance to choose where they want to put their x or o

def user_character_choice():
    
    global p1_choice
    global p2_choice
    
    answer = False
    
    while answer == False:
        
        print(f"Please {player_1} type x or o, to choose your game character")
        p1_choice = input()
        
        if (p1_choice.upper() != 'X') and (p1_choice.upper() != 'O'):
            print(f"Please {player_1} type x or o, to choose your game character")
        elif p1_choice.upper() == 'X': 
            p2_choice = 'O'
            answer=True
        else:
            p2_choice = 'X'
            answer = True
        
        
        
    print(f'{player_1} you have chosen the {p1_choice.upper()} character, so {player_2} you have {p2_choice} character')
        
    return 'Have fun.....'

# asking player to insert a choice

def replace_function():
    
    global where
    
    # requesting a box
    answer = False
    while answer == False:
        
        where = num_position-1
        
        if str(choices[where]).isdigit():
            choices[where] = text
            answer = True
        else:
            print('Sorry this position is taken, please choose another one')
            location_request()
            
# Winning function

def winning_scheme():
    global victories1
    global victories2
    
    for l,j,k in win:
        if choices[l] == p1_choice and choices[j] == p1_choice and choices[k] == p1_choice:

            print(f'Congrats {player_1} for your VICTORY....')
            victories1 = victories1 + 1


            print(f'So far the score is \n{player_1} has {victories1} \n{player_2} has {victories2} \n') 
            i = 0
            exit_plan()

        elif choices[l] == p2_choice and choices[j] == p2_choice and choices[k] == p2_choice:

            print(f'Congrats {player_2} for your VICTORY....')
            victories2 = victories2 + 1


            print(f'So far the score is \n{player_1} has {victories1} \n{player_2} has {victories2} \n')
            i = 0
            exit_plan()

        else:
            pass

#game of the all
global i
i=1

global choices
choices = [1,2,3,4,5,6,7,8,9]

global win
win = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

victories1 = 0
victories2 = 0

global leave
leave = False

#start of the program

names_request()                    #asking for the names of the participants
user_character_choice()            #each participant chooses their character

while leave == False:               
    display_runner()               # display the arena
    location_request()             # location that the player want to play
    replace_function() 
    winning_scheme()    
    i = i + 1

print(f'The final score is {victories1} for {player_1} and {victories2} for {player_2}')

