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
        self._segments = []
        self._prepare_body()

    def get_segments(self):
        return self._segments

    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        return self._segments[0]

    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(constants.GREEN)
            self._segments.append(segment)

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self):
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "#"
            color = constants.YELLOW if i == 0 else constants.GREEN
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)



        # self.set_text("@")
        # self.set_color(constants.GREEN)
        # self.set_font_size(15)

        # x = (self._position.get_x() + self._velocity.get_x()) % constants.MAX_X
        # y = (self._position.get_y() + self._velocity.get_y()) % constants.MAX_Y
        # self._position = Point(x, y)

        # velocity = Point(x, y)
        # velocity = velocity.scale(constants.CELL_SIZE)
        # self.set_velocity(velocity)

        # position = Point(x, y)
        # position = position.scale(constants.CELL_SIZE)
        # self.set_position(position)
