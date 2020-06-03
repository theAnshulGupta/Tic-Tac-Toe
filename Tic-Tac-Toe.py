#tic-tac-toe

board=[0,1,2,3,4,5,6,7,8]

def tic_tac_toe():
    print(board[0], "|", board[1], "|", board[2])
    print("---------")

    print(board[3], "|", board[4], "|", board[5])
    print("---------")

    print(board[6], "|", board[7], "|", board[8])



tic_tac_toe()

while True:
    
    choiceX=int(input("Please select a spot to draw an X.\n"))
    
    if board[choiceX]!="x" and board[choiceX]!='o':
        board[choiceX]="x"
        tic_tac_toe()

##    if ((board[0] and board[1] and board[2])=="x") or ((board[3] and board[4] and board[5])=="x") or ((board[6] and board[7] and board[8])=="x") or ((board[0] and board[3] and board[6])=="x") or ((board[1] and board[4] and board[7])=="x") or ((board[2] and board[5] and board[8])=="x") or ((board[0] and board[4] and board[8])=="x") or ((board[2] and board[4] and board[6])=="x"):
##        print("X wins")
##        break

    if board[0]==board[1]==board[2]=="x":
        print("X wins")
        break
    if board[2]==board[5]==board[8]=="x":
        print("X wins")
        break
        
##    choiceO=int(input("Please select a spot to draw an O.\n"))
##
##    if board[choiceO]!="x" and board[choiceO]!='o':
##        board[choiceO]="o"
##        tic_tac_toe()
##    
