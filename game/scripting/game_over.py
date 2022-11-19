import constants
import time
from game.shared.point import Point
from game.casting.actor import Actor
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.script import Script
from game.services.keyboard_service import KeyboardService
from game.casting.player1 import Player1
from game.casting.player2 import Player2


class Game_Over:
    """Game_Over triggers when a player collides with their opponent's trail...

    =>A "game over" message is displayed in the middle of the screen.
    =>The cycles turn white.
    =>Players keep moving and turning but don't run into each other."""

    def __init__(self):
      self.actor = Actor()
      self.controlactors = ControlActorsAction(KeyboardService)
      self.script = Script()
      self.player1 = Player1()
      self.player2 = Player2()
      print("game over init")

    def do_game_over(self, cast):

        """Shows the 'game over' message and turns the cycles white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        print("do game over method")
        cycle = self.cast.get_first_actor("cycles")
        trail = cycle.get_segments()

        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)
        position = Point(x, y)

        message = Actor()
        message.set_text("Game Over!")
        message.set_position(position)
        cast.add_actor("messages", message)

        for cycle in trail:
            cycle.set_color(constants.WHITE)


        left = Point(-constants.CELL_SIZE, 0)
        right = Point(constants.CELL_SIZE, 0)
        up = Point(0, -constants.CELL_SIZE)
        down = Point(0, constants.CELL_SIZE)
        wait = time.sleep(1)

        self.script.add_action("movement", left)
        self.script.add_action("movement", up)
        self.script.add_action("movement", right)
        self.script.add_action("movement", down)


        while 1:
        #a never-ending loop that keeps the characters running
        #in their own squares

            actions = self.script.get_actions("movement")
            for action in actions:
                self.player1.turn_head
                self.player2.turn_head
                wait