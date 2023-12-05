import os
import random
from time import sleep

board = {
    'a1':' ',
    'a2':' ',
    'a3':' ',
    'b1':' ',
    'b2':' ',
    'b3':' ',
    'c1':' ',
    'c2':' ',
    'c3':' '
}
userIcon = 'X'
aiIcon = 'O'

def check_winner():
    # Sjekk rader
    for i in range(3):
        if board[f'a{i+1}'] == board[f'b{i+1}'] == board[f'c{i+1}'] != ' ':
            return board[f'a{i+1}']

    # Sjekk kolonner
    for i in range(3):
        if board[f'a{i+1}'] == board[f'b{i+1}'] == board[f'c{i+1}'] != ' ':
            return board[f'a{i+1}']

    # Sjekk diagonalene
    if board['a1'] == board['b2'] == board['c3'] != ' ':
        return board['a1']
    if board['a3'] == board['b2'] == board['c1'] != ' ':
        return board['a3']

    return None

def start():
    os.system('cls')

    userIcon=input('Vil du starte som X eller O?')
    if (userIcon == 'X'):
        userIcon = 'X'
        aiIcon = 'O'
    elif (userIcon == 'x'):
        userIcon = 'X'
        aiIcon = 'O'
    elif (userIcon == 'O'):
        userIcon = 'O'
        aiIcon = 'X'
    elif (userIcon == 'o'):
        userIcon = 'O'
        aiIcon = 'X'
    else:
        start()
    humanMove()

def humanMove():
    printBoard()
    empty_positions = [key for key, value in board.items() if value == ' ']
    if empty_positions:
        move = input('Hvor vil du sette ' + userIcon +'? (a1, a2, a3, b1, b2, b3, c1, c2, c3) ')
        if not board[move] == ' ':
            print('Velg en ledig plass')
            firstMove()
        board[move] = userIcon
        printBoard()
        winner = check_winner()
        if winner:
            print(f'{winner} har vunnet!')
            return
        sleep(2)
        os.system('cls')
        aiMove()
    else:
        print('Uavgjort')


def aiMove():
    empty_positions = [key for key, value in board.items() if value == ' ']
    if not empty_positions:
        print('Uavgjort')

    print('Jeg tenker...')
    sleep(random.randint(1, 3))
    
    ai_move = random.choice(empty_positions)
    board[ai_move] = aiIcon
    printBoard()
    winner = check_winner()
    if winner:
        print(f'{winner} har vunnet!')
        return
    os.system('cls')
    humanMove()

def printBoard():
    os.system('cls')
    print(board['a1'],'|',board['a2'],'|',board['a3'])
    print('⎯⎯⎯⎯⎯⎯⎯⎯⎯')
    print(board['b1'],'|',board['b2'],'|',board['b3'])
    print('⎯⎯⎯⎯⎯⎯⎯⎯⎯')
    print(board['c1'],'|',board['c2'],'|',board['c3'])
    return

start()