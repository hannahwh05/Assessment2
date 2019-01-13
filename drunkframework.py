'''
GEOG5990M Programming for Geographical Information Analysis: Core Skills
Drunk Framework for Model

This file contains the code for the Drunk class. This is imported into the
DrunkModel code. 

201284811 Hannah Wheldon
GitHub username: hannahwh05

Version 1.0.0

1. Drunk moves randomly left, right, up, down in loop if proposed movement is 
   less than or equal to the distance to their home.
2. Home distance is determined by the drunk's house coordinates and the x and y
    values of the drunk. This can be either it's current or proposed position.
3. Drunk knows it has reached home once it's current coordinates are equal to 
    it's house door coordinates.
'''

import random

class Drunk():
    """
    Drunk class:
    A class to describe the moment of a drunk person from a pub to their home 
    in a town.
    Characteristics:
        - x-coordinate
        - y-coordinate
        - The values of the environment the drunks "stumble" around in
        - The size of the environment
        - Awareness of other drunks
        - House number/home
        - Knowledge of where the pub door is
        - Knowledge of where its house door is 
        - Distance to it's house door
        - Knows when it has arrived back home
        - An element of randomness to its movements
    """
    def __init__(self, env, route_environ, drunks, houseno, pubDoor, 
                 houseCoords, randomness, x=None, y=None):
        """
        Constructor takes arguments:
        env -- a list (environment) of lists (rowlists), imported from a csv 
               file, creating the 2D landscape in which the drunk exists.
        drunks -- all the agents in the environment.
        houseno -- house number assigned to drunk
        pubDoor -- the coordinates for the pub door at which all drunks begin 
        their journey.
        x -- the x axis coordinate.
        y -- the y axis coordinate.
        """
        self.env = env
        self.route_environ = route_environ
        #Make Drunk aware of the other drunks
        self.drunks = drunks
        self._envWidth = len(env) 
        self._envHeight = len(env[0])
        self._x = pubDoor[0]
        self._y = pubDoor[1]
        self.houseno = houseno
        self.houseCoords = houseCoords
        self.home = False
        self.randomness = randomness
    
    def home_distance(self, houseCoords, X, Y):
        """
        Returns the distance to the drunk's house, using Pythagoras' theorum.
        Input X and Y coordinates of drunk's current or proposed location.
        """
        return ((((houseCoords[0] - X)**2) + 
                 ((houseCoords[1] - Y)**2))**0.5)
     
    def stumble(self):
        """
        Movement of drunk within the environment.
        
        Can change number of spaces to be moved if condtions are met.
        
        Drunk moves along x and y axis dependent on a random number generated.
        Drunk moves right if random number is less than 0.5 
        (random number is between 0.0-1.0), and if the proposed distance to 
        home is equal to or less than the current distance (this gives each 
        drunk some direction to home). Otherwise drunk moves left if the the 
        proposed distance to home is equal to or less than the current 
        distance. This is the same for movements up and down.
        """
        #Can change number of places moved by drunk. Currently a random number
        #between 1 and 5.
        unitsMoveBy = random.randint(1,5)
        #x coordinate of drunk plus a number.
        moveR = self._x + unitsMoveBy
        #x coordinate of drunk minus a number.
        moveL = self._x - unitsMoveBy
        #y coordinate of drunk plus a number.
        moveUp = self._y + unitsMoveBy
        #y coordinate of drunk minus a number.
        moveDown = self._y - unitsMoveBy
        #Distance between drunk's current position and drunk's home.
        currDist = self.home_distance(self.houseCoords, self._x, self._y)
        #Potential distance to drunk's home after move taken below.
        moveRDist = self.home_distance(self.houseCoords, moveR, self._y)
        moveLDist = self.home_distance(self.houseCoords, moveL, self._y)
        moveUpDist = self.home_distance(self.houseCoords, self._x, moveUp)
        moveDownDist = self.home_distance(self.houseCoords, self._x, moveDown)
        #move along x axis i.e. right or left.
        #if random number produced (between 0 and 1) is less than 0.5
        if random.random() < 0.5:
            #and if value of the environment at the location of the drunk 
            #plus a number on the x axis is equal to 0 or house location
            if moveRDist <= currDist or random.random() < self.randomness:
                #then drunk moves right
                self._x = moveR
        elif moveLDist <= currDist or random.random() < self.randomness:
            #then drunk moves left
            self._x = moveL
   
        if random.random() < 0.5:
            if moveUpDist <= currDist or random.random() < self.randomness:
                #then drunk moves up
                self._y = moveUp
        elif moveDownDist <= currDist or random.random() < self.randomness:
            #then drunk moves down
            self._y = moveDown
        #print(self.houseno, currDist) #test
        #Adds 100 to environment at every step
        #n.b. y, x not x, y to be consistent with reversed environment axes
        self.route_environ[self._y][self._x] += 1
        
    def back_home(self):
        """
        Describes if the drunk has reached their home.
        If their current position is the same as their house door coordinates,
        then they have made it home.
        """
        if [self._x, self._y] == self.houseCoords:
            self.home = True
            print(self.houseno, self.houseCoords, 
                  "Finally I'm back! Off to bed!")