import random

# 9 positions

board_positions=['','','','','','','','','','']

def printBoard(bp):
    
    print(' '+board_positions[1]+' | '+board_positions[2]+' | '+board_positions[3]+' ')
    print('___________')
    print()
    print(' '+board_positions[4]+' | '+board_positions[5]+' | '+board_positions[6]+' ')
    print('___________')
    print()
    print(' '+board_positions[7]+' | '+board_positions[8]+' | '+board_positions[9]+' ')

def checkWinner(bp,i):
    if ((bp[1]==i and bp[2]==i and bp[3]==i)or
        (bp[4]==i and bp[5]==i and bp[6]==i)or
        (bp[7]==i and bp[8]==i and bp[9]==i)or
        (bp[1]==i and bp[4]==i and bp[7]==i)or
        (bp[2]==i and bp[5]==i and bp[8]==i)or
        (bp[1]==i and bp[5]==i and bp[9]==i)or
        (bp[3]==i and bp[5]==i and bp[7]==i)or
        (bp[3]==i and bp[6]==i and bp[9]==i)):
        return True
    else:
        return False

def checkEmptySpace(bp,i):
    if bp[i]=='':
        return True
    else:
        return False

def insertLetter(bp,p,i):
    bp[p]=1

def checkFullBoard(bp):
    br=0
    for i in board_positions:
        if i=='':
            br+=1
    if br==1:
        return True
    else:
        return False    

# player X, computer O

def playerMove(bp):
    position=int(input("1-9 "))
    onMove=True
    while onMove:
        if position > 0 and position < 10:
            if checkEmptySpace(bp,position):
                bp[position]='X'
                onMove=False
            else:
                print('Occupied')
                position=int(input("1-9 "))
        else:
            print("1-9 !")
            position=int(input("1-9 "))
    
def compMove(bp):
    possibilities=[]
    for i,j in enumerate(board_positions):
        if j=='' and i!=0:
            possibilities.append(i)

    for i in possibilities:
        br=bp.copy()
        br[i]='X'
        if checkWinner(br,'X'):
            position=i
            return position
    for i in possibilities:
        br=bp.copy()
        br[i]='O'
        if checkWinner(br,'O'):
            position=i
            return position

    ind=random.randint(0,len(possibilities))
    return possibilities[ind]

printBoard(board_positions)
while checkFullBoard(board_positions) == False:
    if checkWinner(board_positions,'O')==False:
        playerMove(board_positions)
    else:
        print('Lost')
        break
    if checkWinner(board_positions,'X')==False:
        if checkFullBoard(board_positions) == False:
            board_positions[compMove(board_positions)]='O'
    else:
        print('Won')
        break
    printBoard(board_positions)
    if checkFullBoard(board_positions) == True:
        print('Tie')
        break
