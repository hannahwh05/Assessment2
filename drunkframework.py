'''
GEOG5990M Programming for Geographical Information Analysis: Core Skills
Drunk Framework for Model

This file contains the code for the Drunk class. This is imported into the
DrunkModel code. 

201284811 Hannah Wheldon
GitHub username: hannahwh05

Version 1.0.0
'''

'''
1. Drunk moves randomly left, right, up, down in loop
2. When it hits the correctly numbered house, stop process and begin with next drunk
3. Add 1 to each point the drunk moves 
4. Stop drunk from retracing steps

'''

import random

#change number of places moved by drunk
unitsMoveBy = 5

class Drunk():
    def __init__(self, env, drunks, houseno, pubDoor, houseCoords, x=None, 
                 y=None):
        self.env = env
        #Make Drunk aware of the other agents
        self.drunks = drunks
        self._envWidth = len(env) 
        self._envHeight = len(env[0])
        self._x = pubDoor[0]
        self._y = pubDoor[1]
        self.houseno = houseno
        self.houseCoords = houseCoords
        self.home = False

      
    def stumble(self):
        #x coordinate of drunk plus a number
        moveR = self._x + unitsMoveBy
        moveL = self._x - unitsMoveBy
        #furthest extent of environment on x axis i.e. far right
        wallX = self._envWidth

        #move along x axis i.e. right or left
        #if random number produced (between 0 and 1) is less than 0.5
        if random.random() < 0.5:
            #and if value of the environment at the location of the drunk 
            #plus a number on the x axis is equal to 0
            if self.env[moveR][self._y] == 0:
                #and within the environment boundary (i.e. if moveR is greater 
                #than or equal to zero and less than or equal to the width of 
                #the environment
                if moveR >=0 and moveR <= wallX:
                    #then drunk moves right
                    self._x = moveR
        #if conditions are not met above then
        #if value of the environment at the location of the drunk 
        #minus a number on the x axis is equal to 0
        elif self.env[moveL][self._y] == 0:
            #and if within environment boundary
            if moveL >=0 and moveL <= wallX:
                #then drunk moves left
                self._x = moveL
        
        #y coordinate of drunk plus a number
        moveUp = self._y + unitsMoveBy
        #y coordinate of drunk minus a number
        moveDown = self._y - unitsMoveBy
        #furthest extent of environment on y axis i.e. top
        wallY = self._envHeight

        #move along y axis i.e. up or down
        #if random number produced (between 0 and 1) is less than 0.5
        if random.random() < 0.5:
            #and if value of the environment at the location of the drunk 
            #plus a number on the y axis is equal to 0
            if self.env[self._x][moveUp] == 0:
                #and if within environment boundary (i.e. if moveUp is greater 
                #than or equal to zero and less than or equal to the height of 
                #the environment
                if moveUp >=0 and moveUp <= wallY:
                    #then drunk moves up
                    self._y = moveUp
        #if conditions are not met above then
        #if value of the environment at the location of the drunk 
        #minus a number on y axis is equal to 0
        elif self.env[self._x][moveDown] == 0:
            #and if within environment boundary
            if moveDown >=0 and moveDown <= wallY:
                #then drunk moves down
                self._y = moveDown

    def home(self):
        if self.env[self._x + 1][self._y] == self.houseCoords:
            [self._x][self._y] = self.houseCoords 

    '''
    def stumble(self):
        """
        Movement of Drunk within the environment.
        Drunk moves along x and y axis dependent on a random number generated.
        Moves +1 space if random number is less than 0.5, otherwise -1 
        space if more than 0.5 (random number is between 0.0-1.0).
        "%" operator keeps the agents within the environment.       
        """

        
        if random.random() < 0.5:
            if self.env[self._x + unitsMoveBy][self._y] == 0:
                self._x = (self._x + unitsMoveBy) % self._envWidth
        elif self.env[self._x - unitsMoveBy][self._y] == 0:
            self._x = (self._x - unitsMoveBy) % self._envWidth
        # Move y i.e. up and down
        if random.random() < 0.5:
            if self.env[self._x][self._y + unitsMoveBy] == 0:
                self._y = (self._y + unitsMoveBy) % self._envHeight
        elif self.env[self._x][self._y - unitsMoveBy] == 0:
            self._y = (self._y - unitsMoveBy) % self._envHeight
        '''

    '''
    def boundary(self):
        # Move x i.e. left and right
        if random.random() < 0.5:
            if [self._x + unitsMoveBy][self._y] >= 299:
                self._x = 299
        elif [self._x - unitsMoveBy][self._y] <= 1:
            self._x = 1
        # Move y i.e. up and down
        if random.random() < 0.5:
            if [self._x][self._y + unitsMoveBy] >= 299:
                self._x = 299
        elif [self._x][self._y - unitsMoveBy] <= 1:
            self._y = 1
    
        
    '''         


             


            
            
