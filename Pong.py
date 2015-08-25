# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_vel = [1, 1]
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    rand_horiz = random.randrange(120, 240)/60.0
    rand_vert = random.randrange(60, 180)/60.0
    if direction == RIGHT:
        ball_vel[0] += rand_horiz
        ball_vel[1] -= rand_vert
    else: 
        ball_vel[0] -= rand_horiz
        ball_vel[1] -= rand_vert

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    paddle1_pos = paddle2_pos = HEIGHT / 2
    paddle1_vel = paddle2_vel = 0
    score1 = score2 = 0
    spawn_ball(LEFT)
    
    
    

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel    
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
       
    # update ball
    ball_pos[0] += ball_vel[0] 
    ball_pos[1] += ball_vel[1] 
   
    if ball_pos[0] >= (WIDTH - PAD_WIDTH - 1) - BALL_RADIUS:
        if paddle2_pos - HALF_PAD_HEIGHT <= ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT:
            ball_vel[0] = -1.1 * ball_vel[0]
        else:
            score1 += 1
            spawn_ball(LEFT)
    elif ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        if paddle1_pos - HALF_PAD_HEIGHT <= ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT:
            ball_vel[0] = -1.1 * ball_vel[0]
        else:
            score2 += 1
            spawn_ball(RIGHT)
    elif ball_pos[1] >= (HEIGHT - 1) - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]    
    
        
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "Yellow", "Yellow")
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    if paddle1_pos <= HALF_PAD_HEIGHT:
        paddle1_pos = HALF_PAD_HEIGHT
    elif paddle1_pos >= HEIGHT - 1 - HALF_PAD_HEIGHT:
        paddle1_pos = HEIGHT - 1 - HALF_PAD_HEIGHT
    
    paddle2_pos += paddle2_vel
    if paddle2_pos <= HALF_PAD_HEIGHT:
        paddle2_pos = HALF_PAD_HEIGHT
    elif paddle2_pos >= HEIGHT - 1 - HALF_PAD_HEIGHT:
        paddle2_pos = HEIGHT - 1 - HALF_PAD_HEIGHT
    
    # draw paddles
    p1_up_left = [0, paddle1_pos - HALF_PAD_HEIGHT]
    p1_up_right = [PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT]
    p1_down_right = [PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT]
    p1_down_left = [0, paddle1_pos + HALF_PAD_HEIGHT]
    
    canvas.draw_polygon([p1_up_left, p1_up_right, p1_down_right, p1_down_left],
                         1, "White", "White")
    
    p2_up_left = [WIDTH - 1 - PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT]
    p2_up_right = [WIDTH - 1, paddle2_pos - HALF_PAD_HEIGHT]
    p2_down_right = [WIDTH - 1, paddle2_pos + HALF_PAD_HEIGHT]
    p2_down_left = [WIDTH - 1 - PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT]
    
    canvas.draw_polygon([p2_up_left, p2_up_right, p2_down_right, p2_down_left],
                         1, "White", "White")
    
    # draw scores
    canvas.draw_text(str(score1), (WIDTH / 4 - 10, 70), 50, "White")
    canvas.draw_text(str(score2), (3 * WIDTH / 4 -10, 70), 50, "White")
        
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel = -10
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel = 10
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel = -10
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel = 10
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel = 0
    paddle2_vel = 0
    
# restart the game
def restart_game():
    new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Restart', restart_game, 100)


# start frame
new_game()
frame.start()
