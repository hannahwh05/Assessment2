# Assessment 2: Planning for drunks - Show me the way to go home...

## 1.	Summary 

Version 1.0.0

This documentation aims to provide an overview of the agent-based model, DrunkModel.py, that was developed for Assessment 2 of  GEOG5990M Programming for Geographical Information Analysis: Core Skills. 

The model simulates a town of 25 drunk people trying to “stumble” back to their homes from the pub. It outputs a density map and .txt file to show where drunks stumbled on their way back to their homes. 

It was developed in Spyder 3.3.2 (Python 3.7) and the following documentation describes how to run it from this IDE. 

There are no further plans for development of this program. 

## 2.	How to Run

Files required to run the model:
* DrunkModel.py – this is the main model from which the program is run,
* Drunkframework.py – this contains the Drunk class and outlines the characteristics of the drunks,
* town_plan.txt – This is a 300 by 300 raster file representing the town in which the drunks stumble about in. The pub is denoted by 1s, the houses by the numbers 10-250, in increments of 10, and everywhere else, zeros. 

These files can be found on my GitHub: https://github.com/hannahwh05/Assessment2

In Spyder set Tools > Preferences > Ipython console > Graphics > Set backend 
to inline.

For this model, town_plan.txt has been used for the environment (Figure 1). The code allows for an alternative csv environment to be imported.

!(hannahwh05.github.io/images/town_plan.png "Figure 1: Town Plan")
      

The simulation is run from tkinter GUI. When the code is run, a window will appear on the computer screen called Drunk Model. To run the model, click "Run" from the "Menu" in this window, as shown in Figure 2.

When the model has met the "stopping condition", where all the drunks have arrived home, as shown in Figure 3a, close the window and a density map showing the points where the drunks have passed through, will be printed to the console and saved as density.png to the current directory, shown in Figure 3b, along with density.txt file containing the density points. 1 is added to every point the drunks pass through. 

## 3.	Program Description

This program does the following:
1.	Pulls in a csv/txt file with values for an environment and finds out the pub point and the home points.
2.	Displays the pub and homes on the screen.
3.	Creates drunks and assigns them a home each.
4.	Animates the drunks leaving the pub and reaching their homes.
5.	Stores how many times drunks pass through each point on the map to a density.txt file.
6.	Displays the density of drunks that have passed through each point on the map and saves it to density.png.


There are 25 drunks, each of which have homes assigned to them according to their number (creation number plus 10 (to match the house number). Houses are labelled 10-250 in increments of 10. The drunks randomly “stumble” left, right, up and down, back to their homes from the pub based on conditions met in a for loop. An element of bias is introduced to give the drunks some direction to their homes and prevent them from retracing their steps (though there is a small probability that they can to increase the randomness of their movements, as described below). For every point that the drunks stumble through on the map, 1 is added to the corresponding value in the density.txt file and therefore the density.png. When the drunk reaches their home, they stop stumbling. They print to the console their house number, door coordinates and announce, "Finally I'm back! Off to bed!". Once all the drunks have arrived back home, "Stopping condition has been met. All drunks are home!", is printed. At this point the animation window can be closed triggering the density data and map to be saved to the current directory. 
Certain elements within the model and framework can be changed to suit the user:
* The environment/town_plan – this is imported based on the numbers of rows and columns in the file. Provided the buildings are square, the coordsFinder function will locate the pub, houses and their doors based on the ID inputs. n.b. if the house numbers are not in the 100s, alter line 129 in DrunkModel.py as appropriate.
* The number of drunks – consequently to the above point, the number of drunks can be changed to match the number of houses within the imported environment.
* The degree of drunkness/randomness of the stumbles – this is dictated by:
  * The “randomness” variable on line 156 of the DrunkModel.py where, randomness = random.random()/3, giving a random number of uniform probability between 0 and 0.3 recurring. The higher the random number the more drunk the Drunk is, where 0 would lead the Drunk directly to their home. 
  * the “unitsMoveBy” variable, on line 88 of the drunkframework.py, where unitsMoveBy = random.randint(1,5), giving a random integer between 1 and 5. 
* The names of the txt and png files can be changed in lines 283 and 301 respectively.


