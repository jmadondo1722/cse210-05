import constants
import time
from game.shared.point import Point
from game.casting.actor import Actor
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.script import Script
from game.services.keyboard_service import KeyboardService
from game.casting.player1 import Player1
from game.casting.player2 import Player2
from game.casting.cast import Cast


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
      self.cast = Cast()
      print("game over init")

    def do_game_over(self, cast, _is_game_over):

        """Shows the 'game over' message and turns the cycles white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        print("do game over method")

        cycles = self.cast.get_actors("player1")
        #need to do again for player2 because they are in 2 different actor groups

        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)
        position = Point(x, y)

        #game over message
        message = Actor()
        message.set_text("Game Over!")
        message.set_position(position)
        cast.add_actor("messages", message)

        #make it all white
        for cycle in cycles:
            trail = cycle.get_segments()
            cycle.set_color(constants.WHITE)
            trail.set_color(constants.WHITE)

        #the different directions
        left = Point(-constants.CELL_SIZE, 0)
        right = Point(constants.CELL_SIZE, 0)
        up = Point(0, -constants.CELL_SIZE)
        down = Point(0, constants.CELL_SIZE)
        wait = time.sleep(1)

        #adding it to script
        self.script.add_action("movement", left)
        self.script.add_action("movement", up)
        self.script.add_action("movement", right)
        self.script.add_action("movement", down)

        if _is_game_over:
            while 1:
            #a never-ending loop that keeps the characters running
            #in their own squares

                actions = self.script.get_actions("movement")
                for action in actions:
                    self.player1.turn_head
                    self.player2.turn_head
                    wait