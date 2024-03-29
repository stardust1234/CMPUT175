class TicTacToe:
    def __init__(self):
        # "board" is a list of 10 strings representing the board (ignore index 0)
        self.board = [" "]*10
        self.board[0]="#"
        #self.board = ['#','x','o','x','o','o','x','x','x','o']
               
        
#------------------------------------------------------------- 
    def drawBoard(self):
    # This method prints out the board with current plays adjacent to a board with index.
        for i in range(len(self.board)):
            self.board[i] = self.board[i].center(3)         
        print('%s|%s|%s'%(self.board[7],self.board[8],self.board[9]), ' 7 | 8 | 9 ', sep= "\t")
        print('-----------','-----------', sep = '\t')
        print('%s|%s|%s'%(self.board[4],self.board[5],self.board[6]), ' 4 | 5 | 6 ', sep= "\t")
        print('-----------','-----------', sep = '\t')
        print('%s|%s|%s'%(self.board[1],self.board[2],self.board[3]), ' 1 | 2 | 3 ', sep= "\t")

#-------------------------------------------------------------         
    def assignMove(self, cell,ch):
        self.board[cell] = ch

#------------------------------------------------------------- 
    def boardFull(self):
        if self.board.count('   ') > 0:
            return False
        else:
            return True

#------------------------------------------------------------- 
    def cellIsEmpty(self, cell):
        if self.board[int(cell)] == '   ':
            return True
        else: return False

#------------------------------------------------------------- 
    def whoWon(self):
    # returns the symbol of the player who won if there is a winner, otherwise it returns an empty string. 
        if self.isWinner("x"):
            return "x"
        elif self.isWinner("o"):
            return "o"
        else:
            return ""

#-------------------------------------------------------------   
    def isWinner(self, ch):
        ch = ch.center(3)
        vertical1 = [self.board[1],self.board[4],self.board[7]]
        vertical2 = [self.board[2],self.board[5],self.board[8]]
        vertical3 = [self.board[3],self.board[6],self.board[9]]
        horizontal1 = [self.board[1],self.board[2],self.board[3]]
        horizontal2 = [self.board[4],self.board[5],self.board[6]]
        horizontal3 = [self.board[7],self.board[8],self.board[9]]
        diagnal1 = [self.board[1],self.board[5],self.board[9]]
        diagnal2 = [self.board[3],self.board[5],self.board[7]]
        #print(diagnal1)
        lines = [vertical1,vertical2,vertical3,horizontal1,horizontal2,horizontal3,diagnal1,diagnal2]
        for i in lines:
            if i.count(ch) == 3:
                return True
        return False
        
    # Given a player's letter, this method returns True if that player has won.

#write some code here
def main():
    myBoard = TicTacToe()
    myBoard.drawBoard()
    iteration = 0
    while myBoard.whoWon() == '':
        if iteration%2 == 0:
            ch = input('It is the turn for x . What is your move?')
            try:
                if int(ch) > 9 or int(ch) < 1:
                    print('Your input is out of bound')
                    continue
                if not myBoard.board[int(ch)].cellIsEmpty():
                    print('Please enter a number that is empty.')
                    continue
            except:
                print('Please enter a number between 1-9')
            myBoard.assignMove(int(ch), 'x')
            iteration += 1
        else:
            ch = input('It is the turn for o . What is your move?')
            try:
                if int(ch) > 9 or int(ch) < 1:
                    print('Your input is out of bound')
                    continue
                if not myBoard.board[int(ch)].cellIsEmpty():
                    print('Please enter a number that is empty.')
                    continue
            except:
                print('Please enter a number between 1-9')
            myBoard.assignMove(int(ch), 'o')
            iteration += 1
        myBoard.drawBoard()
        print('************************************************')
        if myBoard.whoWon() == '' and myBoard.boardFull():
            print('It\' a tie.')
            break
    if myBoard.whoWon() != '':
        print(myBoard.whoWon(), 'wins. Congrats!')
        
main()
