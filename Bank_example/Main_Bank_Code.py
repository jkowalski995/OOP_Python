# Main program for controlling a Bank made up of Accounts
from Bank import *

# Create an instance of the Bank
oBank = Bank('8:30 do 17:30', 'Wodociągowa 2, Toruń, Polska', '888 999 000')

# Main code
while True:
    print()
    print('To get an account balance, press b')
    print('To close an account, press c')
    print('To make a deposit, press d')
    print('To get bank information, press i')
    print('To open a new account, press o')
    print('To quit, press q')
    print('To show all accounts, press s')
    print('To make a withdrawal, press w ')
    print()

    action = input('What do You want to do').lower()[0]  # Get first lowercase letter from input string
    print()

    try:
        if action == 'b':
            oBank.balance()
        elif action == 'c':
            oBank.closeAccount()
        elif action == 'd':
            oBank.deposit()
        elif action == 'i':
            oBank.getInfo()
        elif action == 'o':
            oBank.openAccount()
        elif action == 'q':
            break
        elif action == 's':
            oBank.show()
        elif action == 'w':
            oBank.withdraw()

    except AbortTransaction as error:
        # Print out the error message
        print(error)

print('Done')

