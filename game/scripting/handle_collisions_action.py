import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
from game.scripting.game_over import Game_Over
from game.scripting.script import Script

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self.game_over = Game_Over()

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        print("execute method")
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self.game_over.do_game_over(cast)
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
<<<<<<< HEAD
        #player 1 logic
        player1 = cast.get_first_actor("player1")
        player1_head = player1.get_segments()[0]
        player1_segments = player1.get_segments()[1:]

        #player 2 logic 
        player2 = cast.get_first_actor("player2")
        player2_head = player2.get_segments()[0]
        player2_segments = player2.get_segments()[1:]
        
        #player 1 head collision for player 1 segment
        for segment in player1_segments:
            if player1_head.get_position().equals(segment.get_position()):
                self._is_game_over = True
        
        #player 2 head collision for player 2 segment
        for segment in player2_segments:
            if player2_head.get_position().equals(segment.get_position()):
                self._is_game_over = True
    
        #player 1 head collision for player 2 segment
        for segment in player2_segments:
            if player1_head.get_position().equals(segment.get_position()):
                self._is_game_over = True
    
        #player 2 head collision for player 1 segment
        for segment in player1_segments:
            if player2_head.get_position().equals(segment.get_position()):
                self._is_game_over = True
=======
#         print("handle segment collisions method")
#         snake = cast.get_first_actor("snakes")
#         head = snake.get_segments()[0]
#         segments = snake.get_segments()[1:]
        
#         for segment in segments:
#             #we need to fix this so it works for two players
#             if head.get_position().equals(segment.get_position()):
#                 self._is_game_over = True
# >>>>>>> c835ffb57a7f995385fa06ae618a62ea5e8f1c49
    
            