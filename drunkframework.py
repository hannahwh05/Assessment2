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
unitsMoveBy = random.randint(1,5)

class Drunk():
    def __init__(self, env, drunks, houseno, pubDoor, houseCoords, 
                 x=None, y=None):
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
    
    def home_distance(self, houseCoords, X, Y):
        """
        Returns the distance between the drunk's house and their starting
        point at the pub door, using Pythagoras' theorum.
        """
        return ((((houseCoords[0] - X)**2) + 
                 ((houseCoords[1] - Y)**2))**0.5)
    
    def stumble(self):
        moveR = self._x + unitsMoveBy
        moveL = self._x - unitsMoveBy
        moveUp = self._y + unitsMoveBy
        moveDown = self._y - unitsMoveBy
        currDist = self.home_distance(self.houseCoords, self._x, self._y)
        moveRDist = self.home_distance(self.houseCoords, moveR, self._y)
        moveLDist = self.home_distance(self.houseCoords, moveL, self._y)
        moveUpDist = self.home_distance(self.houseCoords, self._x, moveUp)
        moveDownDist = self.home_distance(self.houseCoords, self._x, moveDown)
        if random.random() < 0.5:
            if moveRDist <= currDist:
                self._x = moveR
        elif moveLDist <= currDist:
            self._x = moveL
        if random.random() < 0.5:
            if moveUpDist <= currDist:
                self._y = moveUp
        elif moveDownDist <= currDist:
            self._y = moveDown
            
            
        
        
        
            
        
    '''       
    #keep to show development of model!!!
    
    def stumble(self):
        #x coordinate of drunk plus a number
        moveR = self._x + unitsMoveBy
        moveL = self._x - unitsMoveBy
        #furthest extent of environment on x axis i.e. far right
        wallX = self._envWidth
        currDist = self.home_distance(self.houseCoords, self._x, self._y)
        moveRDist = self.home_distance(self.houseCoords, moveR, self._y)
        moveLDist = self.home_distance(self.houseCoords, moveL, self._y)
        #move along x axis i.e. right or left
        #if random number produced (between 0 and 1) is less than 0.5
        if random.random() < 0.5:
            #and if value of the environment at the location of the drunk 
            #plus a number on the x axis is equal to 0 or house location
            if moveRDist <= currDist:
                if (self.env[moveR][self._y] == 0 or 
                    self.env[moveR][self._y] == self.houseCoords):
                #and within the environment boundary (i.e. if moveR is greater 
                #than or equal to zero and less than or equal to the width of 
                #the environment
                    if moveR >=0 and moveR <= wallX:
                        #then drunk moves right
                        self._x = moveR
        #if conditions are not met above then
        #if value of the environment at the location of the drunk 
        #minus a number on the x axis is equal to 0 or house location
        elif moveLDist <= currDist:
            if (self.env[moveL][self._y] == 0 or 
                self.env[moveL][self._y] == self.houseCoords):
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
        moveUpDist = self.home_distance(self.houseCoords, self._x, moveUp)
        moveDownDist = self.home_distance(self.houseCoords, self._x, moveDown)
        #move along y axis i.e. up or down
        #if random number produced (between 0 and 1) is less than 0.5
        if random.random() < 0.5:
            #and if value of the environment at the location of the drunk 
            #plus a number on the y axis is equal to 0 or house location
            if moveUpDist <= currDist:
                if (self.env[self._x][moveUp] == 0 or 
                    self.env[self._x][moveUp]== self.houseCoords):
                    #and if within environment boundary (i.e. if moveUp is 
                    #greater than or equal to zero and less than or equal to 
                    #the height of the environment
                    if moveUp >=0 and moveUp <= wallY:
                        #then drunk moves up
                        self._y = moveUp
        #if conditions are not met above then
        #if value of the environment at the location of the drunk 
        #minus a number on y axis is equal to 0 or house location
        elif moveDownDist <= currDist:
            if (self.env[self._x][moveDown] == 0 or 
                self.env[self._x][moveDown] == self.houseCoords):
                #and if within environment boundary
                if moveDown >=0 and moveDown <= wallY:
                    #then drunk moves down
                    self._y = moveDown
        '''
    '''    
    def home(self):
        if self.env == self.houseCoords:
            self.home = True
    '''

             


            
            
