'''
GEOG5990M Programming for Geographical Information Analysis: Core Skills
Drunk Model

201284811 Hannah Wheldon
GitHub username: hannahwh05

Version 1.0.0

*****what the model does*****

1. Import libraries
2. Read in environment file "drink.txt"
3. 

n.b. to run model with random coordinates instead of scraping from webpage, 
remove 3rd and 4th arguements i.e. y, x in Step 4.

****any specific settings needed****

'''

###############################################################################
################################# Import ######################################
###############################################################################
'''import libraries/functions/packages'''

import csv

import drunkframework
import matplotlib
#2D plotting library
import matplotlib.pyplot as plot
#animate plot
import matplotlib.animation as ani
#framework to build tkinter graphics interface
import tkinter
matplotlib.use('TkAgg')
#tkinter backend
import matplotlib.backends.backend_tkagg

num_of_drunks = 25

###############################################################################
#######################'''Step ?: Import environment'''########################
###############################################################################
'''read in raster data from csv'''

f = open('drunk.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

#set up environment container to read data into
environment = []
for row in reader:
    #set up row container	
    rowlist = []		
    for value in row:
        #append values from rows in csv file to rowlist
        rowlist.append(value)
    #append rowlist values from for loop into environment container
    environment.append(rowlist)

#Close the reader    				
f.close()

#test to see environment alone
plot.imshow(environment)
plot.show()

###############################################################################
##########################'''Step 4: Plot agents'''############################
###############################################################################

drunks = []

for i in range(num_of_drunks):
    drunks.append(drunkframework.Drunk(environment, drunks))
'''    
# set up figure size and axes
fig = matplotlib.pyplot.figure(figsize=(8, 8))
ax = fig.add_axes([0, 0, 1, 1])

carry_on = True

def update(frame_number):
    """
    Updates the display in the animation:
    Plot axes based on size of environment.
    Agents move, eat, share with neighbours and vomit.
    """
    #clear previous display           
    fig.clear()
    #create global variable to modify local variable outside of function
    
    global carry_on
  
    #make plot based on size of environment
    plot.xlim(0, len(environment))
    plot.ylim(0, len(environment[0]))
    
    #for each agent - move, eat, share with neighbours and vomit 
    for i in range(num_of_drunks):
        #agents randomly move around environment
        drunks[i].move()

    #plot environment and set minimum and maximum limits based on environment
    # values to prevent scaling of colour when model runs
    #plot.imshow(environment, vmin = 92, vmax= 255)
        
    for i in range(num_of_drunks):
        plot.scatter(drunks[i]._x, drunks[i]._y) 
'''