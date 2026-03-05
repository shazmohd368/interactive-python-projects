'''
Pong – Classic Arcade Game
Rice University: An Introduction to Interactive Programming in Python

This program implements the classic Pong game using the SimpleGUI framework.
Two players control paddles to bounce a ball back and forth. If a player misses
the ball, the opponent scores a point.

Controls:
Player 1: W (up), S (down)
Player 2: Up Arrow (up), Down Arrow (down)
Restart: Restart button
'''

import simplegui
import random

# ---------------------------------------------------------
# Global Constants
# ---------------------------------------------------------

WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80

LEFT = False
RIGHT = True


# ---------------------------------------------------------
# Global Game State Variables
# ---------------------------------------------------------

ball_pos = [WIDTH/2, HEIGHT/2]
vel = [1, 1]

paddle1_pos = 0
paddle2_pos = 0

paddle1_vel = 0
paddle2_vel = 0

score1 = 0
score2 = 0


# ---------------------------------------------------------
# Ball Initialization
# ---------------------------------------------------------

def spawn_ball(direction):
    '''
    Spawns the ball in the center of the screen and assigns
    a random velocity.

    direction:
        RIGHT -> ball moves toward player 2
        LEFT  -> ball moves toward player 1
    '''
    
    global ball_pos
    
    ball_pos = [WIDTH/2, HEIGHT/2]

    if direction == RIGHT:
        vel[0] = 0.01 * random.randrange(120, 240)
        vel[1] = -0.01 * random.randrange(60, 180)

    elif direction == LEFT:
        vel[0] = -0.01 * random.randrange(120, 240)
        vel[1] = -0.01 * random.randrange(60, 180)


# ---------------------------------------------------------
# Game Reset
# ---------------------------------------------------------

def new_game():
    '''
    Resets paddles, scores, and respawns the ball.
    '''
    
    global paddle1_pos, paddle2_pos
    global score1, score2

    score1 = 0
    score2 = 0

    paddle1_pos = HEIGHT/2 - PAD_HEIGHT/2
    paddle2_pos = HEIGHT/2 - PAD_HEIGHT/2

    spawn_ball(random.randrange(0,2))


# ---------------------------------------------------------
# Main Draw Handler
# ---------------------------------------------------------

def draw(canvas):
    '''
    Main game loop.

    Handles:
    - Ball movement
    - Paddle movement
    - Collision detection
    - Score updates
    - Rendering game objects
    '''

    global score1, score2
    global paddle1_pos, paddle2_pos
    global ball_pos, vel
    global paddle1_vel, paddle2_vel

    # Draw center line and gutters
    canvas.draw_line([WIDTH/2, 0], [WIDTH/2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0], [PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0], [WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # -----------------------------------------------------
    # Ball Physics
    # -----------------------------------------------------

    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]

    # Bounce off top and bottom walls
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= (HEIGHT - BALL_RADIUS):
        vel[1] = -vel[1]

    # Draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, 'white', 'white')


    # -----------------------------------------------------
    # Paddle Movement (with boundary limits)
    # -----------------------------------------------------

    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel

    paddle1_pos = max(0, min(HEIGHT - PAD_HEIGHT, paddle1_pos))
    paddle2_pos = max(0, min(HEIGHT - PAD_HEIGHT, paddle2_pos))


    # -----------------------------------------------------
    # Draw Paddles
    # -----------------------------------------------------

    canvas.draw_polygon([[0, paddle1_pos],
                         [PAD_WIDTH, paddle1_pos],
                         [PAD_WIDTH, paddle1_pos + PAD_HEIGHT],
                         [0, paddle1_pos + PAD_HEIGHT]],
                        1, 'WHITE', 'WHITE')

    canvas.draw_polygon([[WIDTH, paddle2_pos],
                         [WIDTH, paddle2_pos + PAD_HEIGHT],
                         [WIDTH - PAD_WIDTH, paddle2_pos + PAD_HEIGHT],
                         [WIDTH - PAD_WIDTH, paddle2_pos]],
                        1, 'WHITE', 'WHITE')


    # -----------------------------------------------------
    # Paddle Collision Detection
    # -----------------------------------------------------

    # Left paddle
    if ball_pos[0] <= (PAD_WIDTH + BALL_RADIUS):

        if paddle1_pos <= ball_pos[1] <= paddle1_pos + PAD_HEIGHT:
            vel[0] = -1.5 * vel[0]

        else:
            score2 += 1
            spawn_ball(RIGHT)

    # Right paddle
    elif ball_pos[0] >= (WIDTH - PAD_WIDTH - BALL_RADIUS):

        if paddle2_pos <= ball_pos[1] <= paddle2_pos + PAD_HEIGHT:
            vel[0] = -1.1 * vel[0]

        else:
            score1 += 1
            spawn_ball(LEFT)


    # -----------------------------------------------------
    # Draw Scores
    # -----------------------------------------------------

    canvas.draw_text(str(score1), [150, 60], 60, 'white')
    canvas.draw_text(str(score2), [450, 60], 60, 'white')


# ---------------------------------------------------------
# Keyboard Controls
# ---------------------------------------------------------

def keydown(key):
    '''
    Handles paddle movement when keys are pressed.
    '''
    
    global paddle1_vel, paddle2_vel

    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = -3
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = 3
    elif key == simplegui.KEY_MAP['w']:
        paddle1_vel = -3
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 3


def keyup(key):
    '''
    Stops paddle movement when keys are released.
    '''

    global paddle1_vel, paddle2_vel

    if key == simplegui.KEY_MAP['up'] or key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0

    elif key == simplegui.KEY_MAP['w'] or key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0


# ---------------------------------------------------------
# Frame Setup
# ---------------------------------------------------------

frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)

frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

frame.add_button('Restart', new_game)


# ---------------------------------------------------------
# Start Game
# ---------------------------------------------------------

frame.start()
new_game()
