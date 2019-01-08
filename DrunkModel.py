'''
GEOG5990M Programming for Geographical Information Analysis: Core Skills
Assignment 2: Drunk Model

201284811 Hannah Wheldon
GitHub username: hannahwh05

Version 1.0.0

This model is run from tkinter GUI. 
When this code is run, a window will will appear on the computer screen called
Drunk Model. To run the model, click "Run" from the "Menu" in this 
window. When the model has met the "stopping condition", close the window and
the figure will be printed to the console. 

n.b. to run model with random coordinates instead of scraping from webpage, 
remove 3rd and 4th arguements i.e. y, x in Step 4.

In Spyder set Tools > Preferences > Ipython console > Graphics > Set backend 
to inline

Use drunkframework.py for drunk class
'''

###############################################################################
################################# Import ######################################
###############################################################################
'''import libraries/functions/packages at top of code'''

#2D plotting library
import matplotlib
import matplotlib.pyplot as plot
#animate plot
import matplotlib.animation as ani
#framework to build tkinter graphics interface
import tkinter
matplotlib.use('TkAgg')
#tkinter backend
import matplotlib.backends.backend_tkagg
#imports agent from separate coded file to prevent repetition
import drunkframework
#imports raster data from csv file
import csv
import numpy as np
import math

###############################################################################
####################'''Step 1: Assign value to variables'''####################
###############################################################################

num_of_drunks = 25


###############################################################################
#######################'''Step 2: Import environment'''########################
###############################################################################
'''read in raster data from csv'''

f = open('drunk.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

#set up environment container to read data into
environment = []
env = environment
for row in reader:
    #set up row container	
    rowlist = []		
    for value in row:
        #append values from rows in csv file to rowlist
        rowlist.append(value)
    #append rowlist values from for loop into environment container
    env.append(rowlist)

#Close the reader    				
f.close()

#len(env) # test to see size of environment based on csv file

#test to see environment alone
#plot.imshow(env)
#plot.show()
#plot.colorbar()

f = open('route_environ.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

route_taken = []
re = route_taken
for row2 in reader:
    #set up row container	
    rowlist2 = []		
    for value in row2:
        #append values from rows in csv file to rowlist
        rowlist2.append(value)
    #append rowlist values from for loop into environment container
    re.append(rowlist)

#Close the reader    				
f.close()

#test to see route_environ
#plot.imshow(re, plot.cm.get_cmap('Blues'))


###############################################################################
##########################'''Step 4: Plot agents'''############################
###############################################################################
# set up container for agents

drunks = []
ID = []
housenoList = []
houseCoordsList = []
pubDoor = []

#Determine where pub is in the environment
def coordsFinder(ID):
    """
    Finds the coordinates for the door of a building. 
    Input ID of building.
    Outputs x,y coordinates of door of building within the environment.
    """
   
    coordsList = []
    #for every row in the .txt file
    for i in range(0,len(env)):
        #for every column in the .txt file
        for j in range(0,len(env[0])):
            #if the value at coordinate [i][j] is equal to ID given
            if env[i][j] == ID: 
                coordsList.append([i,j])
    #Door is in middle of top row of square
    #pubExit = pubCoordsList[9] 
    '''
    Assuming the building is square, this finds the width of the building by
    finding the square root of the length of the coordsList, and dividing by
    two to find the middle point. 
    '''
    Door = coordsList[int(math.sqrt((float(len(coordsList))))/2)] 
    return Door;
    
pubDoor = coordsFinder(1)
#print(pubDoor) #test to see if correct output

#Create list of house numbers by adding 1 and multiplying by 10 to give the 
#same value as within the environment i.e. Drunk 0 has house number 10
for j in range(num_of_drunks):
    houseno = (j+1)*10
    housenoList.append(houseno)
    #print(houseno) # test to see drunks assigned number    

for i in housenoList:
    houseCoordsList.append(coordsFinder(i))
    
#print(houseCoordsList) # test to see if houseCoordsList has appended the
                        # correct coordinates


    
#distList = []
#
#for i in range(num_of_drunks):
#    distList.append(home_distance(houseCoordsList[i], pubDoor))    
#
#print(distList)

#for loop to append environment, drunks and 
for i in range(num_of_drunks):
    drunks.append(drunkframework.Drunk(env, drunks, housenoList[i], pubDoor, 
                                       houseCoordsList[i]))

# set up figure size and axes
fig = matplotlib.pyplot.figure(figsize=(8, 8))
ax = fig.add_axes([0, 0, 1, 1])


def update(frame_number):
    """
    Updates the display in the animation:
    Plot axes based on size of environment.
    Drunks move....
    """
    #clear previous display           
    fig.clear()
    #create global variable to modify local variable outside of function


    #make plot based on size of environment
    plot.xlim(0, len(env))
    plot.ylim(len(env[0]), 0)
    plot.imshow(env, plot.cm.get_cmap('Blues'))
    plot.colorbar()
    #overlay route_environ on top of environment
    #plot.imshow(re, plot.cm.get_cmap('Blues'))
    
    for i in range(num_of_drunks):
        plot.scatter(drunks[i]._x, drunks[i]._y)
        
    #for each agent - move, eat, share with neighbours and vomit 
    for i in range(num_of_drunks):
        #agents randomly move around environment
        drunks[i].stumble()
        #drunks[i].boundary()

###############################################################################
######################'''Step 4: Stopping condition'''#########################
###############################################################################

for i in range(num_of_drunks):
    if drunks[i].home == True:
        print(i, " : Finally I'm back! Off to bed!")
        
'''
for i in range (num_of_drunks):
    while drunks[i].home == False:
        drunks[i].stumble()
        re[drunks[i]._y][drunks[i]._x]=0
        # For agents that made it home, set their arrival status to True to stop the code from rerunning those agents, and tell them to drunkely announce their arrival
        if drunks[i].env[drunks[i]._y][drunks[i]._x] == drunks[i].houseno: # If the agent's location is the same as their house number
            drunks[i].home = True
            print ("Finally I'm back! Off to bed!")
'''


'''
# generator function to set condition for when to stop 
def gen_function(b = [0]):
    """A stopping function for the animation"""
    a = 0
    global carry_on
    while (a < 500) & (carry_on):
        #function returns generator
        yield a			
        a = a + 1
    print("stopping condition")
'''   
###############################################################################
#########################'''Step 5: Run the model'''###########################
############################################################################### 

def run():
    """ Run model to animate plot for GUI interface"""
    global animation
    animation = ani.FuncAnimation(fig, update, repeat=False)
    canvas.draw()

###############################################################################
#########################'''Step 6: GUI Interface'''###########################
###############################################################################
'''use tkinter to make GUI interface and widgets'''

root = tkinter.Tk() 
root.wm_title("Drunk Model")

canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Menu", menu=model_menu)
model_menu.add_command(label="Run", command=run)
model_menu.add_command(label="Close", command=root.destroy)

tkinter.mainloop()

###############################################################################

print("***Thank you for running the model***")