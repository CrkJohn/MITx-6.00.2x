# 6.00.2x Problem Set 2: Simulating robots

import math
import random

#import ps2_visualize
import pylab
import ps2_visualize
##################
## Comment/uncomment the relevant lines, depending on which version of Python you have
##################

# For Python 3.5:
#from ps2_verify_movement35 import testRobotMovement
# If you get a "Bad magic number" ImportError, you are not using Python 3.5 

# For Python 3.6:
from ps2_verify_movement36 import testRobotMovement
# If you get a "Bad magic number" ImportError, you are not using Python 3.6


# === Provided class Position
class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: number representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):  
        return "(%0.2f, %0.2f)" % (self.x, self.y)
##
### === Problem 5
##class RandomWalkRobot(Robot):
##    """
##    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
##    chooses a new direction at random at the end of each time-step.
##    """
##    def updatePositionAndClean(self):
##        """
##        Simulate the passage of a single time-step.
##
##        Move the robot to a new position and mark the tile it is on as having
##        been cleaned.
##        """
##        raise NotImplementedError
##
##
##def showPlot1(title, x_label, y_label):
##    """
##    What information does the plot produced by this function tell you?
##    """
##    num_robot_range = range(1, 11)
##    times1 = []
##    times2 = []
##    for num_robots in num_robot_range:
##        print("Plotting", num_robots, "robots...")
##        times1.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, StandardRobot))
##        times2.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, RandomWalkRobot))
##    pylab.plot(num_robot_range, times1)
##    pylab.plot(num_robot_range, times2)
##    pylab.title(title)
##    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
##    pylab.xlabel(x_label)
##    pylab.ylabel(y_label)
##    pylab.show()
##
##    
##def showPlot2(title, x_label, y_label):
##    """
##    What information does the plot produced by this function tell you?
##    """
##    aspect_ratios = []
##    times1 = []
##    times2 = []
##    for width in [10, 20, 25, 50]:
##        height = 300//width
##        print("Plotting cleaning time for a room of width:", width, "by height:", height)
##        aspect_ratios.append(float(width) / height)
##        times1.append(runSimulation(2, 1.0, width, height, 0.8, 200, StandardRobot))
##        times2.append(runSimulation(2, 1.0, width, height, 0.8, 200, RandomWalkRobot))
##    pylab.plot(aspect_ratios, times1)
##    pylab.plot(aspect_ratios, times2)
##    pylab.title(title)
##    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
##    pylab.xlabel(x_label)
##    pylab.ylabel(y_label)
##    pylab.show()
##    
##
### === Problem 6
### NOTE: If you are running the simulation, you will have to close it 
### before the plot will show up.
##
###
### 1) Write a function call to showPlot1 that generates an appropriately-labeled
###     plot.
###
###       (... your call here ...)
###
##
###
### 2) Write a function call to showPlot2 that generates an appropriately-labeled
###     plot.
###
###       (... your call here ...)
###
