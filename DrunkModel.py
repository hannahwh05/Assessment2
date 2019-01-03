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

###############################################################################
####################'''Step 1: Assign value to variables'''####################
###############################################################################

num_of_drunks = 25
PubID = 1

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
plot.imshow(env)
plot.show()

###############################################################################
##########################'''Step 4: Plot agents'''############################
###############################################################################

# set up container for agents

PubCoordsList = []
drunks = []

#Determine where pub is in the environment
def ExitFinder(PubID):
    for i in range(0,len(env)):
        for j in range(0,len(env[0])):
            if env[i][j] == PubID:
                PubCoordsList.append([i,j])
    #Pub exit is in middle of bottom row of pub
    PubExit = PubCoordsList[9] 

            
# for loop to append x and y classes, read in above, to each agent
for i in range(num_of_drunks):
    drunks.append(drunkframework.Drunk(env, drunks, PubExit))
    #n.b. to run model with random coordinates, instead of scraping from 
    # webpage, remove 3rd and 4th arguements above i.e. x, y
    
# set up figure size and axes
fig = matplotlib.pyplot.figure(figsize=(8, 8))
ax = fig.add_axes([0, 0, 1, 1])

carry_on = True

def update(frame_number):
    """
    Updates the display in the animation:
    Plot axes based on size of environment.
    Drunks move....
    """
    #clear previous display           
    fig.clear()
    #create global variable to modify local variable outside of function
    global carry_on
    
    #make plot based on size of environment
    plot.xlim(0, len(env))
    plot.ylim(0, len(env[0]))

    #for each agent - move, eat, share with neighbours and vomit 
    for i in range(num_of_drunks):
        #agents randomly move around environment
        drunks[i].move()

        #for loop to plot all agents generated
        
    #plot environment and set minimum and maximum limits based on environment
    # values to prevent scaling of colour when model runs
    plot.imshow(env, cmap=plot.cm.get_cmap('Blues', 300))
    plot.colorbar()
    
    for i in range(num_of_drunks):
        plot.scatter(drunks[i]._x, drunks[i]._y)
  
###############################################################################
######################'''Step 4: Stopping condition'''#########################
###############################################################################

# generator function to set condition for when to stop 
def gen_function(b = [0]):
    """A stopping function for the animation"""
    a = 0
    global carry_on
    while (a < 100) & (carry_on):
        #function returns generator
        yield a			
        a = a + 1
    print("stopping condition")
    
###############################################################################
#########################'''Step 5: Run the model'''###########################
############################################################################### 

def run():
    """ Run model to animate plot for GUI interface"""
    global animation
    animation = ani.FuncAnimation(fig, update, 
                frames=gen_function, repeat=False)
    canvas.show()
    
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
