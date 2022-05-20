def printBoard():
    zero = 'X' if xState[0]  else ( 'O' if zState[0] else 0)
    one = 'X' if xState[1]  else ( 'O' if zState[1]  else 1)
    two = 'X' if xState[2]  else ( 'O' if zState[2]  else 2)
    three = 'X' if xState[3]  else ( 'O' if zState[3]  else 3)
    four = 'X' if xState[4]  else ( 'O' if zState[4]  else 4)
    five = 'X' if xState[5]  else ( 'O' if zState[5]  else 5)
    six = 'X' if xState[6]  else ( 'O' if zState[6]  else 6)
    seven = 'X' if xState[7]  else ( 'O' if zState[7]  else 7)
    eight = 'X' if xState[8]  else ( 'O' if zState[8]  else 8)

    print(f' {zero} | {one} | {two} ')
    print(f'___|___|___')
    print(f' {three} | {four} | {five} ')
    print(f'___|___|___')
    print(f' {six} | {seven} | {eight} ')
def sum(a,b,c):
    return (a+b+c)

def checkWin(xState,zState):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if(sum(xState[win[0]],xState[win[1]],xState[win[2]])==3):
            print('X won the match')
            return 1
        if(sum(zState[win[0]],zState[win[1]],zState[win[2]])==3):
            print('Z won the match')
            return 1
    return -1


xState = [0,0,0,0,0,0,0,0,0]
zState = [0,0,0,0,0,0,0,0,0]
print('Welcome to tic tac toi app using python')
turn = 1 #1 for X and 0 for Z

while(True):
    printBoard()
    if (turn ==1):
        print(f"X's chance") 
        val = int(input('Pleace Enter a value '))
        xState[val] = 1
    else:
        print(f"Z's chance")
        val = int(input('Pleace Enter a value '))
        zState[val] = 1
    win = checkWin(xState, zState)
    if (win != -1):
        break
    turn = 1-turn