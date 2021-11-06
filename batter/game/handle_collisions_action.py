import random
from game import constants
from game.action import Action
import sys
from game.point import Point

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

        #If ball bounces off right wall
        if ball.get_position().get_x() == (constants.MAX_X - 1):
            ball.set_velocity(ball.get_velocity().bounce_x())

        # If ball bounces off left wall
        elif ball.get_position().get_x() == 1:
            ball.set_velocity(ball.get_velocity().bounce_x())

        #If ball bounces off paddle
        elif ball.get_position().get_y() == paddle.get_position().get_y() - 1 and ball.get_position().get_x() in range(paddle.get_position().get_x(), paddle.get_position().get_x() + 11):
            ball.set_velocity(ball.get_velocity().bounce_y())
            print('\a') # Plays a PC Beep

        #If ball bounces off floor:
        elif ball.get_position().get_y() == constants.MAX_Y - 1:
            print("Game over thanks for playing!")
            sys.exit()
            

        #If ball bounces off ceiling
        elif ball.get_position().get_y() == 1:
            ball.set_velocity(ball.get_velocity().bounce_y())

        for single_brick in brick:
            if ball.get_position().equals(single_brick.get_position()):
                brick.remove(single_brick)
                ball.set_velocity(ball.get_velocity().bounce_y())