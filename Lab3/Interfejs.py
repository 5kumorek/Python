import Board

print("HI, now you start game aginst computer\n")

while(True):
    sizeBoard=int(input("Could you give me board's size?\n"))
    char = input("'o' or 'x'?\n")
    MyGame = Board.Board(sizeBoard, char)
    while(True):
        while(True):
            y = int(input("Select x coordinate\n"))-1
            x = int(input("Select y coordinate\n"))-1
            if MyGame.checkCoordinates(x,y):
                break
            else:
                print("You chose wrong box. Select again\n\n")
        MyGame.movePlayer(x,y)
        if MyGame.checkPlayersWin():
            MyGame.printBoard()
            print('You win!!\n')
            break
        MyGame.moveCPU()
        MyGame.printBoard()
        if MyGame.checkCPUsWin():
            print('Unfortunately you lose')
            break
    end='0'

    while end!='1' and end!='2':
        end = input("Type 1 to end and 2 to next game\n")

    if end == '2':
        continue
    elif end == '1':
        break
print('Bye')
