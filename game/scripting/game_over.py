import constants
from game.shared.point import Point
from game.casting.actor import Actor
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.script import Script
from game.services.keyboard_service import KeyboardService

class Game_Over:
    """Game_Over triggers when a player collides with their opponent's trail...

    =>A "game over" message is displayed in the middle of the screen.
    =>The cycles turn white.
    =>Players keep moving and turning but don't run into each other."""

    def __init__(self):
      self.actor = Actor()
      self.controlactors = ControlActorsAction(KeyboardService)
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

        while 1:
            self.controlactors.execute(cast, Script)
            #i want to send a list of actions to execute and have that go on a loop
            #i need it to work for both cycles
            #i think the program wants me to send a list of actions through script
            #then send that list to execute