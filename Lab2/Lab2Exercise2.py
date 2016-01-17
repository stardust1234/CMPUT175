# CMPUT 175 Winter 2013 Lab 2 Exercise 2
# This program is used to calculate the worth of an automobile.

class Automobile:

    # Constructor:
    def __init__(self, length, horsepower, color):
        self.__length = length
        self.__horsepower = horsepower
        self.__color = color

    # Returns the length:
    def get_length(self):
        return self.__length

    # Returns the horsepower:
    def get_horsepower(self):
        return self.__horsepower

    # Return the color factor
    def get_color(self):
        # TODO: You must implement this method!
        if self.__color == 'red':
           return 3
        elif self.__color == 'yellow' or self.__color == 'blue':
             return 2
        else:
             return 1

    #Returns the worth:
    def get_worth(self):
        return self.get_color()*self.get_horsepower()*self.get_length()*10

# Main function, which asks the user for the length, horsepower, and color of
# an automobile, and will then print out the worth of that automobile:
def main():
    # TODO: You must implement this function!
    length = 0
    horsePower = 0
    color = ''
    valid = False
    while not valid:
          length = input('Enter automobile\'s length in meters:')
          try:
              length = int(length)
          except:
                 print('Invalid length, calculation canceled.')
                 continue
          horsePower = input('Enter automobile\'s horsepower:')
          try:
              horsePower = int(horsePower)
          except:
                 print('Invalid horse power, calculation canceled.')
                 continue
          color = input('Enter automobile\'s color:')
          valid = True
    autoMobile = Automobile(length,horsePower,color)
    print('This automobile is worth $%d'%(autoMobile.get_worth()))

main()