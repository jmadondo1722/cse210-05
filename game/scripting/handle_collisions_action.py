import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
from game.scripting.game_over import Game_Over
from game.scripting.script import Script
from game.casting.cast import Cast
from game.casting.player1 import Player1
from game.casting.player2 import Player2

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
        #self.cast = Cast()
        self.player1 = Player1()
        self.player2 = Player2()
    

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        #player1 = self.cast.get_first_actor("player1")
        #player2 = self.cast.get_first_actor("player2")
        
        print("grow tail command")
        self.player1.grow_tail(75)
        self.player2.grow_tail(5)
        
        if self._is_game_over:
            self._handle_segment_collision(cast)
            self.game_over.do_game_over(cast, self._is_game_over)
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """

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
    
            