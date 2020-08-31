theBoard = {'top-L':'','top-M':'','top-R':'',
            'mid-L':'','mid-M':'','mid-R':'',
            'low-L':'','low-M':'','low-R':''}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

turn = 'X'

def checkBoard(board):
    ##top
    if board['top-L'] == board['top-M'] and board['top-L'] == board['top-R']:
        return board['top-L']
    ## mid
    elif board['mid-L'] == board['mid-M'] and board['mid- L'] == board['mid-R']:
        return board['mid-L']
    ## low
    elif board['low-L'] == board['low-M'] and board['low-L'] == board['low-R']:
        return board['low-L']
    ## down L
    elif board['top-L'] == board['mid-L'] and board['top-L'] == board['low-L']:
        return board['top-L']
    ## down M
    elif board['top-M'] == board['mid-M'] and board['top-M'] == board['low-M']:
        return board['top-M']
    ## down R
    elif board['top-R'] == board['mid-R'] and board['top-R'] == board['low-R']:
        return board['top-R']\
    ## diag down
    elif board['top-L'] == board['mid-M'] and board['top-L'] == board['low-R']:
        return board['top-L']
    ## diag up
    elif board['low-L'] == board['mid-M'] and board['low-L'] == board['top-R']:
        return board['low-L']
    else:
        return ''
    
def validateMove(move):
    while True:
        if move in theBoard:
            return move
            
                
        else:
            print('Please enter a valid address')
            move = input()



for i in range(9):
    printBoard(theBoard)
    if checkBoard(theBoard) == '':
        pass
    else:
        print(checkBoard(theBoard) + ' WINS!!!!')
    print('Turn for ' + turn + '. Move on which space?')
    move = validateMove(input())

    
    
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    printBoard(theBoard)

