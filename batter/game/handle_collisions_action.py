import random
from game import constants
from game.action import Action

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self,cast):
        """Detects weather the ball hits a wall/ paddle, or a brick
        
        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """

        ball = cast["ball"][0]
        brick = cast["brick"]
        paddle = cast["paddle"][0]
        #if ball.get_position().get_y() >= constants.MAX_Y:
            #return False
        if ball.get_position().get_x() <= 0 or ball.get_position().get_x() >= constants.MAX_X or ball.get_position().get_y() <= 0:
            self.change_direciton(ball)    
        
        if ball.get_position().equals(paddle.get_position()):
            self.change_direciton(ball)

        for single_brick in brick:
            if ball.get_position().equals(single_brick.get_position()):
                self.hit_brick(brick, single_brick)
                self.change_direciton(ball)

    def hit_brick(self,brick,single_brick):
        """Will delete the brick that the ball touched
        
        Args:
            brick (list): The list of bricks on the board
            single_brick (variable): Single brick in the list of bricks
        """
        index = brick.index(single_brick)
        brick.pop(index)
        

    def change_direciton(self,ball):
        """Changes the direction of the ball
        
        Args:
            ball: An instance of ball 
        """
        velocity = ball.get_velocity()
        ball.set_velocity(velocity.reverse())