# Bank that manages a dictionary of Account objects

from Account import *


class Bank:
    def __init__(self, hours, address, phone):
        self.accountsDict = {}
        self.nextAccountNumber = 0
        self.hours = hours
        self.address = address
        self.phone = phone

    def askForValiAccountNumber(self):
        accountNumber = input('What is Your account number?')
        try:
            accountNumber = int(accountNumber)
        except ValueError:
            raise AbortTransaction('The account number must be an integer')
        if accountNumber not in self.accountsDict:
            raise AbortTransaction(f'There is no account: {accountNumber}')
        return accountNumber

    def getUserAccount(self):
        accountNumber = self.askForValiAccountNumber()
        oAccount = self.accountsDict[accountNumber]
        self.askForValidPassword(oAccount)
        return oAccount

    def askForValidPassword(self, oAccount):
        password = input('Please enter your password: ')
        oAccount.checkPasswordMatch(password)

    def createAccount(self, theName, theStartingAmount, thePassword):
        oAccount = Account(theName, theStartingAmount, thePassword)
        newAccountNumber = self.nextAccountNumber
        self.accountsDict[newAccountNumber] = oAccount
        # Increment account number for next new account
        self.nextAccountNumber += 1
        return newAccountNumber

    def openAccount(self):
        print('*** Open Account ***')
        userName = input('Whats is Your name?')
        userStartingAmount = input('How much money to start Your account?')
        userPassword = input('What password would You like to use?')
        userAccountNumber = self.createAccount(userName, userStartingAmount, userPassword)
        print(f'Your new account number is: {userAccountNumber}')

    def closeAccount(self):
        print('*** Close Account ***')
        userAccountNumber = self.askForValiAccountNumber()
        oAccount = self.accountsDict[userAccountNumber]
        self.askForValidPassword(oAccount)
        theBalance = oAccount.getBalance()
        print(f'You have {theBalance} in Your account, which is being returned to You')
        del self.accountsDict[userAccountNumber]
        print('Your account is now closed')

    def balance(self):
        print('*** Get Balance ***')
        oAccount = self.getUserAccount()
        theBalance = oAccount.getBalance()
        print(f'Your balance is {theBalance}')

    def deposit(self):
        print('*** Make Deposit ***')
        oAccount = self.getUserAccount()
        depositAmount = input('Please enter amount to deposit: ')
        theBalance = oAccount.deposit(depositAmount)
        print(f'Deposited {depositAmount}')
        print(f'Your new balance is {theBalance}')

    def withdraw(self):
        print('*** Withdraw ***')
        oAccount = self.getUsersAccount()
        userAmount = input('Please enter the amount to withdraw: ')
        theBalance = oAccount.withdraw(userAmount)
        print(f'Withdrew {userAmount}')
        print(f'Your new balance is {theBalance}')

    def getInfo(self):
        print(f'Hours {self.hours}')
        print(f'Address {self.address}')
        print(f'Phone {self.phone}')
        print(f'We currently have {len(self.accountsDict)} account(s) open.')

    # Special method for Bank administrator only
    def show(self):
        print('*** Show ***')
        print('(This would typically require an admin password)')
        for userAccountNumber in self.accountsDict:
            oAccount = self.accountsDict[userAccountNumber]
            print('Account {userAccountNumber}')
            oAccount.show()
            print()
