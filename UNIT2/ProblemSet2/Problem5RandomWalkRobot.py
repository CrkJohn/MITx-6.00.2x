class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """
    def updatePositionAndClean(self):
        newPosition = self.getRobotPosition().getNewPosition(self.d,self.speed)
        if self.room.isPositionInRoom(newPosition):
            self.setRobotPosition(newPosition)
            self.room.cleanTileAtPosition(newPosition)
        
        self.setRobotDirection(random.randint(0,359))
