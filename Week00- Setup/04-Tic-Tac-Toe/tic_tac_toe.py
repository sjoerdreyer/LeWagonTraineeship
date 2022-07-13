"""
https://www.codewars.com/kata/5b817c2a0ce070ace8002be0/train/python
"""

def display_board(board, width):
    '''
    A tic tac toe funtion to display the board
    '''
    output = ''
    placing_board = board
    for row in range(len(board)//width):
        output += ' '
        if row != max(range(len(board)//width)):
            for v in range(width):
                if max(range(width)) != v:
                    output += f'{placing_board[v]} | '
                else:
                    output += f'{placing_board[v]} '
                    output += '\n'
                    output += '-'*((width*4)-1)
                    output += '\n'
        else:
            for v in range(width):
                if max(range(width)) != v:
                    output += f'{placing_board[v]} | '
                else:
                    output += f'{placing_board[v]} '

        placing_board = placing_board[width:]

    return output
