'''
GEOG5990M Programming for Geographical Information Analysis: Core Skills
Assignment 2: Planning for drunks - Show me the way to go home...

201284811 Hannah Wheldon
GitHub username: hannahwh05

Version 1.0.0

In Spyder set Tools > Preferences > Ipython console > Graphics > Set backend 
to inline.

Use drunkframework.py for the drunk class.

For this model, town_plan.txt has been used for the environment. An alternative 
environment could be imported.

This model is run from tkinter GUI. 
When this code is run, a window will appear on the computer screen called
Drunk Model. To run the model, click "Run" from the "Menu" in this 
window. When the model has met the "stopping condition", close the window and
a density map showing the points where the drunks have passed through,
will be printed to the console. A .txt file with the density points is also 
saved to the current directory. 100 is added to every point the drunks pass 
through.
'''

###############################################################################
################################# Import ######################################
###############################################################################
'''import libraries/functions/packages at top of code'''

#framework to build tkinter graphics interface
import tkinter
#2D plotting library
import matplotlib
matplotlib.use('TkAgg')
#tkinter backend
import matplotlib.backends.backend_tkagg
import matplotlib.pyplot as plt
#animate plot
import matplotlib.animation as ani
import IPython
#imports agent from separate coded file to prevent repetition
import drunkframework
#imports raster data from csv file
import csv
import os
import math
import random

###############################################################################
####################'''Step 1: Assign value to variables'''####################
###############################################################################

num_of_drunks = 25

###############################################################################
#######################'''Step 2: Import environment'''########################
###############################################################################
'''read in town plan raster data from csv'''

f = open('town_plan.txt', newline='') 
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
#plt.imshow(env)
#plt.colorbar()

###############################################################################
################'''Step 3: Find coordinates in environment'''##################
###############################################################################
'''set up containers'''

drunks = []
ID = []
housenoList = []
houseCoordsList = []
pubDoor = []

def coordsFinder(ID):
    """
    Finds the coordinates for the door of a building. 
    Input ID of building.
    Outputs x,y coordinates of door of building within the environment.
    """
    coordsList = []
    #for every row in the town_plan.txt file
    for i in range(0,len(env)):
        #for every column in the town_plan.txt file
        for j in range(0, len(env[0])):
            #if the value at coordinate [j][i] is equal to ID given
            if env[j][i] == ID: 
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

###############################################################################
###########'''Step 4: Create environment to add density data to'''#############
###############################################################################
                        
#container for routes taken
route_environ = []
#create empty environment to append values, to show points drunks have passed 
#through, later on in code
for i in range(0,len(env)):
    rowlist = []
    for j in range(0, len(env[0])):
        rowlist.append(0)
    route_environ.append(rowlist)


#for loop to append environment and drunks
for i in range(num_of_drunks):
    randomness = random.random()/3
    drunks.append(drunkframework.Drunk(env, route_environ, drunks, 
                                       housenoList[i], pubDoor, 
                                       houseCoordsList[i], randomness))

#set map inline
shell = IPython.get_ipython()
shell.enable_matplotlib(gui='inline')

#set up figure size and axes
fig = plt.figure(figsize=(8, 8))
ax = fig.add_axes([0, 0, 1, 1])

carry_on = True

##container to append the town plan to the density map
#densityTP = []
#
##create empty environment to append routes taken by drunks, later on in code
#for i in range(300):
#    rowlist = []
#    for j in range(300):
#        #rowlist.append(env[i][j]+route_environ[i][j])
#                rowlist.append(route_environ[i][j])
#    densityTP.append(rowlist)

###############################################################################
########################'''Step 5: Create animation'''#########################
###############################################################################
    
def update(frame_number):
    """
    Updates the display in the animation:
    Plot axes based on size of environment.
    Drunks move and stop once they are back home.
    """
    #clear previous display           
    fig.clear()
    
    global carry_on
    
    no_of_drunks_home = 0

    for i in range(num_of_drunks):
        if drunks[i].home==True:
            no_of_drunks_home += 1
            
    if no_of_drunks_home == num_of_drunks:
        carry_on = False
    
    for i in range(num_of_drunks):
        #drunks move around environment
        #drunks[i].stumble()
        #drunks[i].back_home() 
        
        if drunks[i].home==False:
            drunks[i].stumble()
            drunks[i].back_home()
    
    #make plot based on size of environment 
    plt.xlim(0, len(env))
    #coordinates are reversed on y axis so environment is displayed as in 
    #town_plan.txt file
    plt.ylim(len(env[0]), 0)
    #colour environment using blues colour scheme
    plt.imshow(env, plt.cm.get_cmap('Blues'))
    #create legend
    plt.colorbar()
    #overlay route_environ on top of environment
    #plt.imshow(densityTP, plt.cm.get_cmap('Blues'))
    
    #plot all the drunks
    for i in range(num_of_drunks):
        plt.scatter(drunks[i]._x, drunks[i]._y)
    
###############################################################################
######################'''Step 6: Stopping condition'''#########################
###############################################################################
       
# generator function to set condition for when to stop 
def gen_function(b = [0]):
    """A stopping function for the animation"""
    a = 0
    global carry_on
    while (a < 500) & (carry_on):
        #function returns generator
        yield a			
        a = a + 1
    print("Stopping condition has been met. All drunks are home!")
  
###############################################################################
#########################'''Step 7: Run the model'''###########################
############################################################################### 

def run():
    """ Run model to animate plot for GUI interface"""
    global animation
    animation = ani.FuncAnimation(fig, update, 
                frames=gen_function, repeat=False)
    canvas.draw()

###############################################################################
#########################'''Step 8: GUI Interface'''###########################
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
###################'''Step 9: Save density map to csv'''#######################
###############################################################################

#saves density data to current file directory as "density" text file
#n.b. this can be changed to .csv
csvfile = os.path.dirname(os.path.abspath(__file__))+"\density.txt"

with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(route_environ)

#set map inline
shell = IPython.get_ipython()
shell.enable_matplotlib(gui='inline')

# set up figure size and axes
fig = matplotlib.pyplot.figure(figsize=(8, 8))
ax = fig.add_axes([0, 0, 1, 1])
#display map
plt.title('Density Map of Drunks')
plt.imshow(route_environ)# plt.cm.get_cmap('binary'))
plt.colorbar()
#save as .png
plt.savefig('density.png', bbox_inches = 'tight')

print("***Thank you for running the model***")