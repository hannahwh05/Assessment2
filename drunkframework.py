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
        
    def stumble(self):
        xmove = self._x + 1
        wallX = self._envWidth - 1
        if random.random() < 0.5:
            if self.env[self._x + unitsMoveBy][self._y] == 0:
                if xmove >=0 and xmove <= wallX:
                    self._x = (self._x + unitsMoveBy)
        elif self.env[self._x - unitsMoveBy][self._y] == 0:
            if xmove >=0 and xmove <= wallX:
                self._x = (self._x - unitsMoveBy)
        # Move y i.e. up and down
        ymove = self._y + 1
        wallY = self._envHeight - 1
        if random.random() < 0.5:
            if self.env[self._x][self._y + unitsMoveBy] == 0:
                if ymove >=0 and ymove <= wallY:
                    self._y = (self._y + unitsMoveBy)
        elif self.env[self._x][self._y - unitsMoveBy] == 0:
            if ymove >=0 and ymove <= wallY:
                self._y = (self._y - unitsMoveBy)

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
    
    def home(self):
        if self.env[self._x + 1][self._y] == self.houseCoords:
            [self._x][self._y] = self.houseCoords         
    '''    
    
'''
        if random.random() < 0.5:
            if self.env[self._x][self._y + unitsMoveBy] == 0:
                self._y = (self._y + unitsMoveBy) % self._envHeight
        elif self.env[self._x][self._y - unitsMoveBy] == 0:
            self._y = (self._y - unitsMoveBy) % self._envHeight           
    
        if self._x < 0:
            self._x = 0
        if self._y < 0:
            self._y = 0
        if self._x > self.envWidth:
            self._x = self.envWidth
        if self._y > self.envHeight:
            self._y = self.envHeight            
'''
'''       
    def distance_between(self, agents_row_b):
        """
        Returns the distance between row a and row b using Pythagoras theorum.
        """
        return (((self._x - agents_row_b._x)**2) +
                ((self._y - agents_row_b._y)**2))**0.5
'''               


            
            
