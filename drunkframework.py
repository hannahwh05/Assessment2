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
        - House number/home
        - *****************
    """
    def __init__(self, env, route_env, drunks, houseno, pubDoor, houseCoords, 
                 x=None, y=None):
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
        self.route_env = route_env
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
            if moveRDist <= currDist:
                #then drunk moves right
                self._x = moveR
        elif moveLDist <= currDist:
            #then drunk moves left
            self._x = moveL
   
        if random.random() < 0.5:
            if moveUpDist <= currDist:
                #then drunk moves up
                self._y = moveUp
        elif moveDownDist <= currDist:
            #then drunk moves down
            self._y = moveDown
        #print(self.houseno, currDist) #test
        
        self.route_env[self._y][self._x] += 100
        


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
        
  
'''                
    ####test to see where they think houseCoords are
    def stumble(self):
        #change number of places moved by drunk
        unitsMoveBy = random.randint(1,5)
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
                self._x = 138
        elif moveLDist <= currDist:
            self._x = 138
        if random.random() < 0.5:
            if moveUpDist <= currDist:
                self._y = 138
        elif moveDownDist <= currDist:
            self._y = 138
        print(self.houseno, currDist)
'''            
        
        
            
        
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

             


            
            
