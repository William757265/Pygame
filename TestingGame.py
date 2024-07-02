import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
FPS = 60
DOT_RADIUS = 10
DOT_COLOR = (255, 0, 0)  # Red color
DOT_SPEED = 5
GRAVITY = 0.5
JUMP_STRENGTH = -9
PLATFORM_WIDTH = 1000000
PLATFORM_HEIGHT = 20
PLATFORM_COLOR = (0, 0, 0)  
PLATFORM_Y = SCREEN_HEIGHT // 2 + 100  
BLOCK_WIDTH = 20
BLOCK_HEIGHT = 60
BLOCK_COLOR = (0, 0, 255)  
BLOCK_X = 400
BLOCK_Y = 442
BLOCK2_WIDTH = 20
BLOCK2_HEIGHT = 60
BLOCK2_COLOR = (0, 0, 255)  
BLOCK2_X = 600
BLOCK2_Y = 442
SCROLL_SPEED = 6  


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Demo')


clock = pygame.time.Clock()


font = pygame.font.Font(None, 36)


MENU = 0
GAME = 1
GAME_OVER = 2

current_state = MENU


def start_game():
    global current_state
    current_state = GAME


def reset_game():
    global dot_x, dot_y, dot_velocity_y
    dot_x = SCREEN_WIDTH // 40
    dot_y = PLATFORM_Y - DOT_RADIUS
    dot_velocity_y = 0


dot_x = SCREEN_WIDTH // 40
dot_y = PLATFORM_Y - DOT_RADIUS
dot_velocity_y = 0


platform_x = SCREEN_WIDTH // 2 - PLATFORM_WIDTH // 2


running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if current_state == MENU:
                start_button_rect = pygame.Rect(300, 400, 200, 50)
                if start_button_rect.collidepoint(event.pos):
                    start_game()
            elif current_state == GAME_OVER:
                reset_game()
                start_game()

    
    keys = pygame.key.get_pressed()
    if current_state == GAME:
        if keys[pygame.K_SPACE] and dot_y + DOT_RADIUS == PLATFORM_Y:
            dot_velocity_y = JUMP_STRENGTH
        if keys[pygame.K_a]:
            dot_x -= DOT_SPEED
        if keys[pygame.K_d]:
            dot_x += DOT_SPEED

        
        dot_velocity_y += GRAVITY
        dot_y += dot_velocity_y

        
        platform_x -= SCROLL_SPEED
        BLOCK_X -= SCROLL_SPEED
        BLOCK2_X -= SCROLL_SPEED

        
        if platform_x + PLATFORM_WIDTH < 0:
            platform_x = SCREEN_WIDTH
        if BLOCK_X + BLOCK_WIDTH < 0:
            BLOCK_X = SCREEN_WIDTH
        if BLOCK2_X + BLOCK2_WIDTH < 0:
            BLOCK2_X = SCREEN_WIDTH

        
        if dot_y + DOT_RADIUS > PLATFORM_Y and platform_x < dot_x < platform_x + PLATFORM_WIDTH:
            dot_y = PLATFORM_Y - DOT_RADIUS
            dot_velocity_y = 0

        
        if dot_x - DOT_RADIUS < 0:
            dot_x = DOT_RADIUS
        if dot_x + DOT_RADIUS > SCREEN_WIDTH:
            dot_x = SCREEN_WIDTH - DOT_RADIUS

       
        dot_rect = pygame.Rect(dot_x - DOT_RADIUS, dot_y - DOT_RADIUS, DOT_RADIUS * 2, DOT_RADIUS * 2)
        block_rect = pygame.Rect(BLOCK_X, BLOCK_Y, BLOCK_WIDTH, BLOCK_HEIGHT)
        block2_rect = pygame.Rect(BLOCK2_X, BLOCK2_Y, BLOCK2_WIDTH, BLOCK2_HEIGHT)

        if dot_rect.colliderect(block_rect) or dot_rect.colliderect(block2_rect):
            current_state = GAME_OVER

    
    screen.fill(WHITE)

    if current_state == MENU:
       
        start_button_rect = pygame.Rect(300, 400, 200, 50)
        pygame.draw.rect(screen, BLACK, start_button_rect)
        start_text = font.render("Start", True, WHITE)
        screen.blit(start_text, (355, 415))

    elif current_state == GAME:
        
        pygame.draw.rect(screen, PLATFORM_COLOR, (platform_x, PLATFORM_Y, PLATFORM_WIDTH, PLATFORM_HEIGHT))

        
        pygame.draw.rect(screen, BLOCK_COLOR, (BLOCK_X, BLOCK_Y, BLOCK_WIDTH, BLOCK_HEIGHT))

        
        pygame.draw.rect(screen, BLOCK2_COLOR, (BLOCK2_X, BLOCK2_Y, BLOCK2_WIDTH, BLOCK2_HEIGHT))

        
        pygame.draw.circle(screen, DOT_COLOR, (dot_x, dot_y), DOT_RADIUS)

    elif current_state == GAME_OVER:
        # Display game over text
        game_over_text = font.render("Game Over", True, BLACK)
        screen.blit(game_over_text, (320, 300))
        restart_text = font.render("Click to Restart", True, BLACK)
        screen.blit(restart_text, (290, 350))

    
    pygame.display.flip()

   
    clock.tick(FPS)


pygame.quit()
sys.exit()


