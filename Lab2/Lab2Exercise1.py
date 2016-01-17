#-------------------------------------------------------------------------------
# Name:        Lab 2 Exercise 1
# Purpose:
#
# Author:      yizhou
#
# Created:     14/01/2016
# Copyright:   (c) yizhou 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def readFile(accountFile):
    validAccounts = {}
    for i in accountFile.readlines():
        name = i.split(':')[0]
        try:
            balance = float(i.split(':')[1])
            validAccounts[name] = balance
        except:
               print('Account for %s not added: illegal value for balance' % (name))
    return validAccounts

def main():
    programEnd = False
    try:
        accountFile = open('accounts.txt')
    except:
           print("Sorry, we cannot find the accounts file.\nThe program will be terminated")
           programEnd = True
    validAccounts = readFile(accountFile)

    while not programEnd:
          validName = False
          account = input('Enter account name, or \'Stop\' to exit: ')
          if account == 'Stop':
             break
          for i in validAccounts.keys():
              if i == account:
                 validName = True
          if validName == False:
             print('Account does not exist, transaction canceled.')
             continue
          try:
              transaction = float(input('Enter transaction amount: '))
          except:
                 print('Illegal value for transaction, transaction canceled')
                 continue
          validAccounts[account] += transaction
          balance = str(validAccounts[account])[:str(validAccounts[account]).find('.')+3]
          print('New balance for account %s: %s'%(account, balance))

if __name__ == '__main__':
    main()
