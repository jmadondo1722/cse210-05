import constants
from game.shared.point import Point
from game.casting.actor import Actor

class Game_Over:
    """Game_Over triggers when a player collides with their opponent's trail...

    =>A "game over" message is displayed in the middle of the screen.
    =>The cycles turn white.
    =>Players keep moving and turning but don't run into each other."""


def handle_game_over(self, cast):
        """Shows the 'game over' message and turns the cycles white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        cycle = cast.get_first_actor("cycles")
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