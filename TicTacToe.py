#Copy your code from Complete the Game or Tic Tac Toe with Random NPC
#use the random class to generate random numbers
import random
#Global Variables
board = [["-","-","-"],["-","-","-"],["-","-","-"]]
player = "X"
turn = int(0)

#Functions
#copy and paste your print_board function definition here!


#returns true if a row,col on the board is open
def is_valid_move(row,col,player):
        
    #elif row != type(int) or col != type(int):
        #print("Input must be an integer!")
        #print()
        #return False
        
    if row < 0 or row > 2 or col < 0 or col > 2:
        print("Input must be within 0 to 2!")
        print()
        return False
        
    elif board[row][col] != "-":
        if player == "X":
            print("Placement Already Taken!")
            print()
        return False
    
    elif row >=0 and row <= 2 and col >= 0 and col <= 2:
        return True

        
#Asks the user to enter a row and col until the user enters a valid location
#Adds user location to the board, and prints the board
def take_turn(player,depth):
    while True:
        print()
        print(player + "'s turn")
        
        if player == "X" :
            try:
                row = int(input("Enter a row "))
            except ValueError: 
                print("Input Again")
                row = int(input("Enter a row "))
            try:
                col = int(input("Enter a col "))
            except ValueError: 
                print("Input Again")
                col = int(input("Enter a col "))
        elif player == "O": 
            #row = random.randrange(0,3)
            #col = random.randrange(0,3)
            score, row, col = minimax("O")
            
            
        else:
            print("Take Turn Netiher Player True Error")
            
        if is_valid_move(row,col,player):
            print()
            place_player(player, row, col)
            break

def print_board():
    print("\tWelcome to Tic Tac Toe!")
    print("")

    #Top of the board
    print("\t0 \t1 \t2")

    #Loop for the board creation
    for i in range(3):
        print(str(i) + "\t- \t- \t-")    
   
#________________________________________________________________
#Then copy your completed minimax from Getting the Row Col Values
depth = 4
num = 0
save = 0

def check_col_win(player):
    if (board[0][0] == player and board[1][0] == player and board[2][0] == player) or (board[0][1] == player and board[1][1] == player and board[2][1] == player) or (board[0][2] == player and board[1][2] == player and board[2][2] == player) :  
        print(player + " Win Col")
        return True
    else:
        return False
        
def check_row_win(player):
    if (board[0][0] == player and board[0][1] == player and board[0][2] == player) or (board[1][0] == player and board[1][1] == player and board[1][2] == player) or (board[2][0] == player and board[2][1] == player and board[2][2] == player) :
        print(player + " Win Row")
        return True
    else:
        return False
        
def check_diag_win(player):
    if (board[0][0] == player and board[1][1] == player and board[2][2] == player) or (board[0][2] == player and board[1][1] == player and board[2][0] == player) :
        print(player + " Win Diag")
        return True
    else:
        return False

def check_win(player):
    if check_col_win(player) == True or check_row_win(player) == True or check_diag_win(player) == True:
        return True
    else:
        return False

def check_tie(player):
    for i in range (3):
        for j in range(3):
            if board[i][j] == "-":
                return False
                
    return True
    
def print_all(player):
    for i in range (3):
        for j in range (3):
            print ("board",i,j, " - ",board[i][j]) 
    
##Copy over your place_player function
def place_player(player, row, col):
    
    ##print ("board[row][col] row col player [place_player1] = ", board[row][col], row, col, player)
    #####wait = input("Press Enter to continue-1.\n")
    
    # !!!!!!!!
    # board[row][col] = player
    ##print ("board[row][col] row col player [place_player2] = ", board[row][col], row, col, player)
  
    if player == "-":
        board[row][col] = player
    
    
    
    if board[row][col] != "-":
        if player == "X":
            print("Placement Already Taken!")
            print()
        return False
        
    elif board[row][col] == "-":
        board[row][col] = player

    #print("<<< Put >>>")
    
    print("")
    #Top of the board
    print("\t0 \t1 \t2")
    
    for i in range(3):
        for j in range(1):
            print(str(i) + "\t" + board[i][j] + "\t" + board[i][j+1] + "\t" + board[i][j+2])
    
    return True        

def minimax(player, depth=5,alpha=-1000, beta=1000):
    
    optimalRow = -1
    optimalCol = -1
   
    if check_win("O") == True:
        print ("<<< Check Win O True >>>")
        return (10, None, None)
        
    elif check_win("X") == True:
        print ("<<< Check Win X True >>>")
        return (-10, None, None)
        
    elif check_tie(player) == True or depth == 0:
        print ("<<< Check_Tie True 01>>>")
        return (0, None, None)


    #print ("<<< player " + player + " >>>")    
    #print_all(player)

    
    #implement recursive case
    print("------------")
    if player == "O":
        j = 1
        best = -10000
        for row in range(3):
            
            j += 1
            print(j)
            
            for col in range(3):
                #print ("board[row][col] row col player [minimax1] = ", board[row][col], row, col, player)
  
                if place_player("O",row,col):
                    #a,b,c = minimax("O", save) 
                    #best = min(best, a)
                    newbest = max(best, minimax("X",(depth -1),alpha, beta)[0], alpha)
                    
                    if newbest > alpha:
                        alpha = newbest
                    
                    if newbest > best:
                        optimalRow = row
                        optimalCol = col
                     
                    best = newbest
                        
                    board[row][col] = "-"
                        
                    if alpha > beta:
                        break
                    

                #print ("board[row][col] row col player [minimax2] = ", board[row][col], row, col, player,"\n\n")
                
                #if board[row][col] == "-":
                    #print("Placement Already Taken! O")
                    #print("yes1")
                    
                if check_tie == True:
                    return (best, optimalRow, optimalCol)
                    
        

        #place_player("-",row,col)
        #print("round O")
        return (best, optimalRow, optimalCol)

    if player == "X":
        i=2
        worst = 10000
        for row in range(3):
            print(i + 1)
            for col in range(3):
                
                if place_player("X",row,col):
                    #x, y, z = minimax("O", save) 
                    #worst = min(worst, x)
                    newworst = min(worst, minimax("O",(depth -1), alpha, beta)[0],beta)
                    
                    if newworst < beta:
                        beta = newworst
                    
                    if newworst < worst:
                        optimalRow = row
                        optimalCol = col
                    
                    worst = newworst
                    board[row][col] = "-"
                    
                    if alpha > beta:
                        break
                
                #if board[row][col] != "-":
                    #print("Placement Already Taken! X")
                    #print("yes2")
                if check_tie == True:
                    return (worst, optimalRow, optimalCol)
                    

        #place_player("-",row,col)
        #print("round X")
        return (worst, optimalRow, optimalCol)



#__________________________________________________________________________




#Start of program
print_board()


while check_win(player) == False:
    turn = turn + 1
    if turn % 2 == 0:
        player = "O"
        
    else:
        player = "X"
    
    take_turn(player, depth)
    if check_tie(player) == True:
        break