import random

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
#-------------------------------------------------------------
class DumbComputer:
      def __init__(self, ch, myBoard):
          self.ch = ch
          self.myBoard = myBoard

      def assignMove_location(self):
          for i in range(1,10):
              if self.myBoard.cellIsEmpty(i):
                 return i
#-------------------------------------------------------------
class RandomComputer:
    def __init__(self, ch, myBoard):
        self.ch = ch
        self.myBoard = myBoard

    def assignMove_location(self):
        cell = random.randint(1,9)
        while not self.myBoard.cellIsEmpty(cell):
            cell = random.randint(1,9)
        return cell
#-------------------------------------------------------------
class SmartComputer:
    def __init__(self, ch, myBoard):
        self.ch = ch
        self.myBoard = myBoard

    def find_oppo_ch(self):
        if self.ch == 'o':
            return 'x'
        else:
            return 'o'

    def find_win(self,ch):
        ch = ch.center(3)
        vertical1 = [1,4,7]
        vertical2 = [2,5,8]
        vertical3 = [3,6,9]
        horizontal1 = [1,2,3]
        horizontal2 = [4,5,6]
        horizontal3 = [7,8,9]
        diagnal1 = [1,5,9]
        diagnal2 = [3,5,7]
        lines = [vertical1,vertical2,vertical3,horizontal1,horizontal2,horizontal3,diagnal1,diagnal2]
        for i in lines:
            line = [self.myBoard.board[i[0]],self.myBoard.board[i[1]],self.myBoard.board[i[2]]]
            if line.count(ch) == 2 and line.count('   ') == 1:
                return i[line.index('   ')]
        return ''
    def check_corner(self):
        for i in [1,3,7,9]:
            if self.myBoard.cellIsEmpty(i):
                return i
        return ''

    def assignMove_location(self):
        oppo_ch = self.find_oppo_ch()
        if self.find_win(self.ch) != '':
            return self.find_win(self.ch)
        if self.find_win(oppo_ch) != '':
            return self.find_win(oppo_ch)
        if self.myBoard.cellIsEmpty(5):
            return 5
        if self.check_corner() != '':
            return self.check_corner()
        cell = random.randint(1,9)
        while not self.myBoard.cellIsEmpty(cell):
            cell = random.randint(1,9)
        return cell

#-------------------------------------------------------------
def printInfo():
    print('Welcome to Tic Tac Toe Series')
    print('User against user..................1')
    print('User against dumb computer.........2')
    print('User against random computer.......3')
    print('User against smart computer........4')
    print('Randomly selected game.............5')
    print('Quit...............................6')
#-------------------------------------------------------------
def makeChoiceOfMode():
    mode = input('Enter your choice')
    while mode not in '123456':
          print('You need to make a valid choice between 1 to 6!!!')
          mode = input('Enter your choice')
    return mode
#-------------------------------------------------------------
def makeChoiceOfCh():
    mode = input('Do you want to play x or o?')
    while mode not in 'xo':
          print('You need to make a valid choice between x or o!!!')
          mode = input('Do you want to play x or o?')
    return mode
#-------------------------------------------------------------
def determineAI(mode,ch_user2, myBoard):
    if mode == '2':
       AI = DumbComputer(ch_user2,myBoard)
    elif mode == '3':
        AI = RandomComputer(ch_user2, myBoard)
    elif mode == '4':
        AI = SmartComputer(ch_user2, myBoard)
    elif mode == '5':
         AI = determineAI(str(random.randint(2,4)), ch_user2, myBoard)
    return AI

#write some code here
def main():
    printInfo()
    myBoard = TicTacToe()
    myBoard.drawBoard()
    iteration = 0
    mode = makeChoiceOfMode()
    if mode in '2345':
        ch_user1 = makeChoiceOfCh()
        if ch_user1 =='x':
            ch_user2 = 'o'
        else: ch_user2 = 'x'
    AI = determineAI(mode, ch_user2, myBoard)
# P v AI mode
    while myBoard.whoWon() == '' and mode not in '16':
          if iteration%2 == 0 and ch_user1 == 'x':
             ch = input('It is the turn for x . What is your move?')
             try:
                 if int(ch) > 9 or int(ch) < 1:
                    print('Your input is out of bound')
                    continue
                 if not myBoard.cellIsEmpty(int(ch)):
                    print('Please enter a number that is empty.')
                    continue
             except:
                    print('Please enter a number between 1-9')
             myBoard.assignMove(int(ch), 'x')
             iteration += 1
          if iteration%2 == 1 and ch_user1 == 'o':
             ch = input('It is the turn for o . What is your move?')
             try:
                 if int(ch) > 9 or int(ch) < 1:
                    print('Your input is out of bound')
                    continue
                 if not myBoard.cellIsEmpty(int(ch)):
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
          if iteration%2 == 1 and ch_user2 == 'o' and not myBoard.boardFull():
             myBoard.assignMove(AI.assignMove_location(), 'o')
             iteration += 1
          if iteration%2 == 0 and ch_user2 == 'x' and not myBoard.boardFull():
             myBoard.assignMove(AI.assignMove_location(), 'x')
             iteration += 1
          myBoard.drawBoard()
          print('************************************************')
          if myBoard.whoWon() == '' and myBoard.boardFull():
             print('It\' a tie.')
             break
# PvP mode
    while myBoard.whoWon() == '' and mode == '1':
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
    if mode != '6':
        if myBoard.whoWon() != '':
            print(myBoard.whoWon(), 'wins. Congrats!')

main()