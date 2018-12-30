'''
GEOG5990M Programming for Geographical Information Analysis: Core Skills
Drunk Model

201284811 Hannah Wheldon
GitHub username: hannahwh05

Version 1.0.0

*****what the model does*****

n.b. to run model with random coordinates instead of scraping from webpage, 
remove 3rd and 4th arguements i.e. y, x in Step 4.

****any specific settings needed****

'''

###############################################################################
################################# Import ######################################
###############################################################################
'''import libraries/functions/packages at top of code'''

import csv
#2D plotting library
import matplotlib.pyplot as plot

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
