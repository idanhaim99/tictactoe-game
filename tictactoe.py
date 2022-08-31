

board=[["1","|","2","|","3","|","4","|","5"],
       ["-","-","-","-","-","-","-","-","-","-"],
       ["6","|","7","|","8","|","9","|","10"],
       ["-","-","-","-","-","-","-","-","-","-"],
       ["11","|","12","|","13","|","14","|","15"],
       ["-","-","-","-","-","-","-","-","-","-"],
       ["16","|","17","|","18","|","19","|","20"],
       ["-","-","-","-","-","-","-","-","-","-"],
       ["21","|","22","|","23","|","24","|","25"]]



def print_board(board):
    for i in board:
        for b in i:
            print(b,end="")
        print("")

def can_play(board):
    for row in range(0,9,2):
        for i in range(0,9,2):
            if board[row][i] != "o"  and board[row][i] != "x" :
                return True
    return False

def player_move(board):
    move=input("enter your move ..")
    for row in range(0,9,2):
        for i in range(0,9,2):
            if board[row][i]==str(move):
                board[row][i]="x"
                return print()
    print("not found")
    player_move(board)

def evaluate(board) :
    for row in range(0,9,2):
        if (board[row][0]==board[row][2]==board[row][4]==board[row][6]==board[row][8]):	
            if (board[row][0] == "o"):
                return 10
            elif (board[row][0] == "x"):
                return -10

    for line in range(0,9,2):
	
        if (board[0][line]==board[2][line]==board[4][line]==board[6][line]==board[8][line]) :
        
            if (board[0][line] == "o") :
                return 10
            elif (board[0][line] == "x") :
                return -10

    if (board[0][0]==board[2][2]==board[4][4]==board[6][6]==board[8][8]) :

        if (board[0][0] == "o") :
            return 10
        elif (board[0][0] == "x") :
            return -10

    if (board[0][8]==board[2][6]==board[4][4]==board[6][2]==board[8][0]) :

        if (board[0][8] == "o") :
            return 10
        elif (board[0][8] == "x") :
            return -10
    return 0

def minimax(board, isMax) :
    score1 = evaluate(board)
    if (score1 == 10) :
        return score1 

    if (score1 == -10) :
        return score1 

    if (can_play(board) == False) :
        return 0

    if (isMax) :	
        best=-1000

        for i in range(0,9,2) :		
            for j in range(0,9,2) :
                if (board[i][j]!='x' and board[i][j]!='|' and board[i][j]!='| ' and board[i][j]!='o') :
                    colval = board[i][j]
                    board[i][j] = "o"
                    score = minimax(board, False)
                    board[i][j] = colval
                    if(score > best):
                        best = score
        return best

    else :
        best=1000

        for i in range(0,9,2) :		
            for j in range(0,9,2) :
                if (board[i][j]!='o' and board[i][j]!='|' and board[i][j]!='| ' and board[i][j]!='x') :
                    colval = board[i][j]
                    board[i][j] = "x"
                    score = minimax(board, True)
                    board[i][j] = colval
                    if score < best:
                        best = score
                    
        return best


def findBestMove(board) :
    bestVal = -1000
    bestMove = (-1,-1)

    for i in range(0,9,2) :	
        for j in range(0,9,2) :
            if (board[i][j]!='x' and board[i][j]!='|' and board[i][j]!='| ' and board[i][j]!='o') :
                colval = board[i][j]
                board[i][j] = "o"
                moveVal = minimax(board, False)
                board[i][j] = colval
                if (moveVal > bestVal) :			
                    bestMove = (i, j)
                    bestVal = moveVal
                if(moveVal==10 or moveVal==0):
                    return bestMove

    return bestMove

def minmax_move(board):
    move = findBestMove(board)
    board[move[0]][move[1]]="o"
    print_board(board)

def check_board(board):
    for row in range(0,5,2):
        if board[row][0]==board[row][2]==board[row][4]==board[row][6]==board[row][8]:
            if board[row][0]=="x":
                return print("you won!!")
            elif board[row][0]=="o":
                return print("ai won!!")

    for line in range(0,5,2):
        if board[0][line]==board[2][line]==board[4][line]==board[6][line]==board[8][line]:
            if board[0][line]=="x":
                return print("you won!!")
            elif board[0][line]=="o":
                return print("ai won!!")
    
    if board[0][0]==board[2][2]==board[4][4]==board[6][6]==board[8][8]:
        if board[0][0]=="x":
            return print("you won!!")
        elif board[0][0]=="o":
            return print("ai won!!")
    
    if board[0][8]==board[2][6]==board[4][4]==board[6][2]==board[8][0]:
        if board[0][4]=="x":
            return print("you won!!")
        elif board[0][4]=="o":
            return print("ai won!!")
    if not can_play(board):
        return print("it is a drow!")

print_board(board)
print()

while True:
    
    player_move(board)
    print()
    check_board(board)
    minmax_move(board)
    check_board(board)
    print()
    
    
    







    

    