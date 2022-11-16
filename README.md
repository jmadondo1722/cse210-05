# cse210-05
The README.md for designing this week's Team Assignment. Enter your name below when you are able to access: 
Kelton Webb: * email: *

Josiah Madondo: * email: jmadondo1722@gmail.com*

Teigen Barber: * email: barber.teigen@gmail.com *

Stacie Abbey: * email: srabbey@byui.edu *


Rules:

Cycle is played according to the following rules:

Players can move up, down, left and right...

    =>Player one moves using the W, S, A and D keys.
    =>Player two moves using the I, K, J and L keys.

Each player's trail grows as they move.
Players try to maneuver so the opponent collides with their trail.
If a player collides with their opponent's trail...

    =>A "game over" message is displayed in the middle of the screen.
    =>The cycles turn white.
    =>Players keep moving and turning but don't run into each other.

Design:
    Casting:
    classes:
        Actor (Parent):(Kelton)
          A visible, moveable thing that participates in the game.

          methods:
            -get_color(self):
            -get_font_size(self):
            -get_position(self):
            -get_text(self):
            -get_velocity(self):
            -move_next(self):
            -set_color(self, color):
            -set_position(self, position):
            -set_font_size(self, font_size):
            -set_text(self, text):
            -set_velocity(self, velocity):

            -Player 1(child class)
            -Player 2(child class)

        Cast:
          A collection of actors.

          methods:
            -add_actor(self, group, actor):
            -get_actors(self, group):
            -get_all_actors(self):
            -get_first_actor(self, group):
            -remove_actor(self, group, actor):

        Snake(Parent):(Josiah)
          A long limbless reptile.

          methods:
            -get_segments(self):
            -move_next(self):
            -get_head(self):
            -grow_tail(self, number_of_segments):
            -turn_head(self, velocity):
            -_prepare_body(self):

                -Player 1(child class)
                -Player 2(child class)

          
    
    Directing:
    Classes:
        Director:
          A person who directs the game.

          methods:
            -start_game(self, cast, script):
            -_execute_actions(self, group, cast, script):

    Scripting:
    Classes:
        Action:
          A thing that is done.

          method:
            -execute(self, cast, script):

        Control_actors_action:
          An input action that controls the snake.

          methods:
            -execute(self, cast, script):

        Draw_actors_action:
          An output action that draws all the actors.

          methods:
            -execute(self, cast, script):

        Handle_collisions_action:
          An update action that handles interactions between the actors.

          methods:
            -execute(self, cast, script):
            -_handle_food_collision(self, cast):
            -_handle_segment_collision(self, cast):
            -_handle_game_over(self, cast):
            
        Move_actors_action:
          An update action that moves all the actors.

          methods:
            -execute(self, cast, script):

        Script:
          A collection of actions.
          methods:
            -add_action(self, group, action):
            -get_actions(self, group):
            -remove_action(self, group, action):

    Services:
    classes:


        Keyboard_service:
          Detects player input.

          methods:
            -is_key_up(self, key):
            -is_key_down(self, key):

        Video_service:
          Outputs the game state. The responsibility of the class of objects is to draw the game state 
    on the screen.

          methods:
            -close_window(self):
            -clear_buffer(self):
            -draw_actor(self, actor, centered=False):
            -draw_actors(self, actors, centered=False):
            -flush_buffer(self):
            -is_window_open(self):
            -open_window(self):
            -_draw_grid(self):
            - _get_x_offset(self, text, font_size):


    Shared:
    classes:

        Color:
          A color.

          methods:
            -to_tuple(self):
            
        Point:
          A distance from a relative origin (0, 0).

          methods:
            -add(self, other):
            -equals(self, other):
            -get_x(self):
            -get_y(self):
            -reverse(self):
            -scale(self, factor):

        Game_over:(Teigen)
         
         methods:
         -display game over message
         -turn the cycles white
         -make them move around not colliding





      ***__main__.py***
      ***constants***