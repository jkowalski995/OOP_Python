# Example of making list of objects
# List of objets is very usefully when we are handling a lot of instances of the same type (enemies in games etc.)
import random

class Monster:
    def __init__(self, nRows, nCols, maxSpeed):
        self.nRows = nRows  # save away
        self.nCols = nCols  # save away
        self.myRow = random.randrange(self.nRows)  # chooses a random row
        self.myCol = random.randrange(self.nCols)  # chooses a random col
        self.mySpeedX = random.randrange(-maxSpeed, maxSpeed + 1)  # chooses an X speed
        self.mySpeedY = random.randrange(-maxSpeed, maxSpeed + 1)  # chooses a Y speed
        # set other instance variables like health, power, etc.

    def move(self):
        self.myRow = (self.myRow + self.mySpeedX) % self.nRows
        self.myCol = (self.myCol + self.mySpeedY) % self.nCols


# Main code
N_MONSTERS = 20
N_ROWS = 100  # could be any size
N_COLS = 200  # could be any size
MAX_SPEED = 4

monsterList = []  # start with an empty list
for i in range(N_MONSTERS):
    oMonster = Monster(N_ROWS, N_COLS, MAX_SPEED)  # create a Monster
    monsterList.append(oMonster)  # add Monster to our list

# Later when playing the game...

for oMonster in monsterList:
    oMonster.move()

