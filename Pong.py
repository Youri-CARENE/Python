import pygame

# Initialize Pygame
pygame.init()

# Set the window dimensions
window_width = 800
window_height = 600

# Create the game window
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Pong Game")

# Set the ball dimensions and starting position
ball_width = 20
ball_height = 20
ball_x = int(window_width / 2 - ball_width / 2)
ball_y = int(window_height / 2 - ball_height / 2)

# Set the ball speed and direction
ball_speed_x = 3
ball_speed_y = 3

# Set the paddle dimensions and starting position
paddle_width = 15
paddle_height = 100
paddle_speed = 5
left_paddle_x = 50
left_paddle_y = int(window_height / 2 - paddle_height / 2)
right_paddle_x = window_width - 50 - paddle_width
right_paddle_y = int(window_height / 2 - paddle_height / 2)

# Set the font for the score
score_font = pygame.font.Font(None, 50)

# Set the initial scores
left_player_score = 0
right_player_score = 0

# Define a function to draw the ball
def draw_ball(ball_x, ball_y):
    pygame.draw.rect(game_window, (255, 255, 255), (ball_x, ball_y, ball_width, ball_height))

# Define a function to draw the paddles
def draw_paddles():
    pygame.draw.rect(game_window, (255, 255, 255), (left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(game_window, (255, 255, 255), (right_paddle_x, right_paddle_y, paddle_width, paddle_height))

# Define a function to update the ball position
def update_ball_position(ball_x, ball_y, ball_speed_x, ball_speed_y):
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_x <= 0:
        ball_x = int(window_width / 2 - ball_width / 2)
        ball_y = int(window_height / 2 - ball_height / 2)
        ball_speed_x = -ball_speed_x
        right_player_score += 1

    if ball_x + ball_width >= window_width:
        ball_x = int(window_width / 2 - ball_width / 2)
        ball_y = int(window_height / 2 - ball_height / 2)
        ball_speed_x = -ball_speed_x
        left_player_score += 1

    if ball_y <= 0 or ball_y + ball_height >= window_height:
        ball_speed_y = -ball_speed_y

    return ball_x, ball_y, ball_speed_x, ball_speed_y, left_player_score, right_player_score

# Define a function to update the paddle position
def update_paddle_position():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        left_paddle_y -= paddle_speed

    if keys[pygame.K_s]:
        left_paddle_y += paddle_speed

    if keys[pygame.K_UP]:
        right_paddle_y -= paddle_speed

    if keys[pygame.K_DOWN]:
        right_paddle_y += paddle_speed

    if left_paddle_y <= 0:
        left_paddle_y = 0

    if left_paddle_y + paddle_height >= window_height:
        left_paddle_y = window_height - paddle_height

    if right_paddle_y

