#-------------------------------------------------------------------------------
# Name:        Assignment 3 - Ocean Treasures
# Purpose:
#
# Author:      Zhao
#
# Created:     24/02/2016
# Copyright:   (c) Zhao 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random, math

class OceanTreasures:
    def __init__(self):
        self.__row = 15
        self.__column = 60
        self.__sonar = 20
        self.__board = self.__createBoard()
        self.__chests = self.generateTreasures()
        self.drawBoard()

    def __createBoard(self):
        board = []
        for row in range(self.__row):
            row = ['~']*self.__column
            board.append(row)
        return board

    def drawBoard(self):
        tens = '   '
        numbers = '   '
        for i in range(self.__column):
            numbers += str(i%10)
            if i%10 == 0 and i >0:
                tens += str(i//10)
            else:
                tens += ' '
        print(tens)
        print(numbers)
        for row in range(self.__row):
            content = ''
            for i in self.__board[row]:
                content+= i
            print('%2s %s %s'%(str(row),content,str(row)))
        print(numbers)
        print('You have %d sonar devices available. Treasures found: %d. Still to be found: %d.'%(self.__sonar, 3-self.getTreasureLeft(), self.getTreasureLeft()))

    def generateTreasures(self):
        treasures = []
        for i in range(3):
            x = random.randint(0,59)
            y = random.randint(0,14)
            treasures.append((x,y))
        while treasures[0] == treasures[1]:
            treasures.remove(0)
            x = random.randint(0,59)
            y = random.randint(0,14)
            treasures.append((x,y))
        while treasures[0] == treasures[2]:
            treasures.remove(0)
            x = random.randint(0,59)
            y = random.randint(0,14)
            treasures.append((x,y))
        while treasures[2] == treasures[1]:
            treasures.remove(1)
            x = random.randint(0,59)
            y = random.randint(0,14)
            treasures.append((x,y))
        return treasures

    def getSonar(self):
        return self.__sonar

    def getChests(self):
        return self.__chests

    def getTreasureLeft(self):
        return len(self.__chests)

    def isDisplayed(self, x, y):
        return self.__board[y][x] != '~'

    def checkDistance(self, x, y):
        dis = 1000
        symbol = 'O'
        verti = '*abcde'
        for i in self.__chests:
            vertical_dis = abs(y - i[1])
            horizontal_dis = abs(x - i[0])
            if vertical_dis > 5 or horizontal_dis > 9:
                continue
            distance = math.sqrt((vertical_dis*2)+(horizontal_dis**2))
            dis = min(dis,distance)
            if dis == distance:
                if horizontal_dis < 2*vertical_dis and horizontal_dis != 0:
                    symbol = str(horizontal_dis)
                else:
                    symbol = verti[vertical_dis]
                    if vertical_dis == 0:
                        symbol = str(horizontal_dis)
            if vertical_dis==0 and horizontal_dis == 0:
                symbol = 'X'
                self.__chests.remove(i)
        return symbol

    def dropSonar(self,x,y,sonar):
        self.__board[y][x] = sonar
        self.__sonar -= 1

def getCoordinate(choice_str):
    a = []
    try:
        c_list = choice_str.split(' ')
        for i in c_list:
            if i != '':
                a.append(int(i))
    except ValueError:
        raise ValueError
    return a

def printHelp():
    print('---------------------------------------------------------------------------------------------------------------')
    print('You have a total of 20 sonar devices and there are 3 treasure chests to find, randomly scattered in the ocean.')
    print('The game ends when you do not have sonar devices left or you found all three chests. To find a chest you need')
    print('to drop a sonar device at the exact x,y coordinates of the chest. In that case the sonar would indicate "X".')
    print('The sonar devices are twice as sensitive on the column axis than the rows. It can detect a chest 9 units away')
    print('on both sides of the x axis and 5 units away on the y axis. If the sonar is dropped too far (more than 9 units')
    print('away on the x axis and 6 on the y axis) from a chest, the sonar would indicate "O", meaning nothing detected.')
    print('Again, the maximum range of the sonar device is 9 units on the x axis and 5 units on the y axis. If the sonar')
    print('is less than 10 units away from a chest on the x axis, the sonar would indicate the distance (1, 2, ..., 9).')
    print('Since the the sonar devices are twice as sensitive on the column axis than the rows, on the y axis (rows), if')
    print('the sonar device is closer than 6 units, closer on the y than half the x axis, and still in the range, the sonar')
    print('would indicate a for 1, b for 2, c for 3, d for 4 and e for 5 distance units.')
    print('---------------------------------------------------------------------------------------------------------------')

def main():
    oceanTresure = OceanTreasures()
    choice = ''
    while not (oceanTresure.getTreasureLeft() == 0 or oceanTresure.getSonar()==0):
        try:
            choice = input('Where do you want to drop your sonar?\nEnter coordinates x y (x in [0..59] and y in [0..14]) (or Q to quit and H for help): ')
            if choice == '':
                raise ValueError
            if choice == 'Q':
                print('The chests were in:', oceanTresure.getChests())
                print('Thank you for playing Ocean Treasures')
                break
            if choice == 'H':
                printHelp()
                continue
            choice = getCoordinate(choice)
        except ValueError:
            print('Your input is invalid. Please check it again')
        if oceanTresure.isDisplayed(choice[0],choice[1]):
            print('You already dropped a sonar there. You lost another sonar device')
        sonar = oceanTresure.checkDistance(choice[0],choice[1])
        oceanTresure.dropSonar(choice[0],choice[1],sonar)
        oceanTresure.drawBoard()
        if oceanTresure.getTreasureLeft() == 0:
            print('Well done! You found all the 3 treasure Chests using %d out of 20 sonar devices.'%(oceanTresure.getSonar()))
    if oceanTresure.getSonar() == 0:
        print('You lost all your 20 sonar devises.')
        print('The remaining chests were in:',oceanTresure.getChests())




if __name__ == '__main__':
    main()