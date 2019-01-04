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

class Drunk():
    def __init__(self, env, drunks, pubExit, x=None, y=None):
        self.env = env
        #Make Drunk aware of the other agents
        self.drunks = drunks
        self._envWidth = len(env) 
        self._envHeight = len(env[0])
        self._x = pubExit[0]
        self._y = pubExit[1]
    
    def stumble(self):
        """
        Movement of Drunk within the environment.
        Drunk moves along x and y axis dependent on a random number generated.
        Moves +1 space if random number is less than 0.5, otherwise -1 
        space if more than 0.5 (random number is between 0.0-1.0).
        "%" operator keeps the agents within the environment.       
        """
        if random.random() < 0.5:
            if self.env[self._x + 1][self._y] == 0:
                self._x = (self._x + 1) % self._envWidth
        elif self.env[self._x - 1][self._y] == 0:
            self._x = (self._x - 1) % self._envWidth
        # Move y i.e. up and down
        if random.random() < 0.5:
            if self.env[self._x][self._y + 1] == 0:
                self._y = (self._y + 1) % self._envHeight
        elif self.env[self._x][self._y - 1] == 0:
            self._y = (self._y - 1) % self._envHeight
