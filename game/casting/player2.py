import constants

from game.casting.actor import Actor
from game.shared.point import Point


class Player1(Actor):
    """Responsible of Player 1's appearance, postition, 
    2d velocity and space.
    Attributes:
        _text (string): The text to display
        _font_size (int): font size to use
        _color (Color): Color of text
        _position (Point): The screen coordinates
        _velocity (Point): speed and direction
    """
    def __init__(self):
        """Constructs Player1"""
        super().__init__()
        
        self.set_text("&")
        self.set_color(constants.RED)
        self.set_font_size(15)
        x = (self._position.get_x() + self._velocity.get_x()) % constants.MAX_X
        y = (self._position.get_y() + self._velocity.get_y()) % constants.MAX_Y
        # self._position = Point(x, y)

        velocity = Point(x, y)
        velocity = velocity.scale(constants.CELL_SIZE)
        self.set_velocity()

        position = Point(x, y)
        position = position.scale(constants.CELL_SIZE)
        self.set_position(position)
