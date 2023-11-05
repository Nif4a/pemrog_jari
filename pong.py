import pygame
import random
pygame.init()

# Set up screen 
screen_width = 800
screen_height = 480
border_size = 10
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# Set up paddles
paddle_width = 20
paddle_height = 150
paddle_speed = 5
left_paddle_x = border_size + 5
right_paddle_x = screen_width - border_size - paddle_width - 5
paddle_y = (screen_height - paddle_height) // 2
right_paddle_y = (screen_height - paddle_height) // 2

# Set up ball
ball_size = 15
directions = [1, -1]
ball_speed_x = random.choice(directions) * 5
ball_speed_y = random.choice(directions) * 5
ball_x = (screen_width - ball_size) // 2
ball_y = (screen_height - ball_size) // 2

font = pygame.font.Font(None, 72)
# display scores
score_A = 0
score_B = 0
def display_scores(score_A, score_B):
    text = font.render(f"{score_A} : {score_B}", True, WHITE)
    text_rect = text.get_rect(center=(screen_width // 2, 30))
    screen.blit(text, text_rect)

# main
running = True
game_started = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if not game_started:
                    ball_speed_x = random.choice(directions) * 5
                    ball_speed_y = random.choice(directions) * 5
                    game_started = True

    keys = pygame.key.get_pressed()

    # paddle posisi
    if keys[pygame.K_w] and paddle_y > 0:
        paddle_y -= paddle_speed
    if keys[pygame.K_s] and paddle_y < screen_height - paddle_height:
        paddle_y += paddle_speed

    if keys[pygame.K_UP] and right_paddle_y > 0:
        right_paddle_y -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle_y < screen_height - paddle_height:
        right_paddle_y += paddle_speed

    # ball posisi
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Collisions walls
    if ball_x <= border_size:
        score_B += 1
        ball_x = (screen_width - ball_size) // 2
        ball_y = (screen_height - ball_size) // 2
        ball_speed_x = 0
        ball_speed_y = 0
        game_started = False
    elif ball_x >= screen_width - ball_size - border_size:
        score_A += 1
        ball_x = (screen_width - ball_size) // 2
        ball_y = (screen_height - ball_size) // 2
        ball_speed_x = 0
        ball_speed_y = 0
        game_started = False

    # collision ball
    if ball_y <= border_size or ball_y >= screen_height - ball_size - border_size:
        ball_speed_y = -ball_speed_y

    # collisions paddles
    if (ball_x <= left_paddle_x + paddle_width and ball_y + ball_size >= paddle_y and ball_y <= paddle_y + paddle_height) or \
            (ball_x + ball_size >= right_paddle_x and ball_y + ball_size >= right_paddle_y and ball_y <= right_paddle_y + paddle_height):
        ball_speed_x = -ball_speed_x

    # screen
    # Define colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    screen.fill(WHITE)  # Fill the screen with white color
    pygame.draw.rect(screen, BLACK, (border_size, border_size, screen_width - 2 * border_size, screen_height - 2 * border_size))
    pygame.draw.rect(screen, WHITE, (border_size, border_size, screen_width - 2 * border_size, screen_height - 2 * border_size), 1)
    pygame.draw.rect(screen, WHITE, (left_paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, WHITE, (right_paddle_x, right_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, WHITE, (ball_x, ball_y, ball_size, ball_size))
    display_scores(score_A, score_B)  # Display scores on the screen

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
