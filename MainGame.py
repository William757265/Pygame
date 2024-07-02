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
PLATFORM_COLOR = (0, 0, 0)  # Black color
PLATFORM_Y = SCREEN_HEIGHT // 2 + 100  # Platform position
BLOCK_WIDTH = 20
BLOCK_HEIGHT = 60
BLOCK_COLOR = (0, 0, 255)  # Blue color
BLOCK_X = 400
BLOCK_Y = 442
BLOCK2_WIDTH = 20
BLOCK2_HEIGHT = 60
BLOCK2_COLOR = (0, 0, 255)  # Blue color
BLOCK2_X = 600    
BLOCK2_Y = 442
SCROLL_SPEED = 0  # Speed at which the world scrolls

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Demo')

# Set up the clock for managing the frame rate
clock = pygame.time.Clock()

# Initial dot position (centered above the platform)
dot_x = SCREEN_WIDTH // 40
dot_y = PLATFORM_Y - DOT_RADIUS
dot_velocity_y = 0

# Platform position
platform_x = SCREEN_WIDTH // 2 - PLATFORM_WIDTH // 2

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key press handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and dot_y + DOT_RADIUS == PLATFORM_Y:
        dot_velocity_y = JUMP_STRENGTH
    if keys[pygame.K_a]:
        dot_x -= DOT_SPEED
    if keys[pygame.K_d]:
        dot_x += DOT_SPEED

    # Apply gravity
    dot_velocity_y += GRAVITY
    dot_y += dot_velocity_y

    # Scroll the world
    platform_x -= SCROLL_SPEED
    BLOCK_X -= SCROLL_SPEED

    # Regenerate platform and block when they go off-screen
    if platform_x + PLATFORM_WIDTH < 0:
        platform_x = SCREEN_WIDTH
    if BLOCK_X + BLOCK_WIDTH < 0:
        BLOCK_X = SCREEN_WIDTH

    # Prevent the dot from falling through the platform
    if dot_y + DOT_RADIUS > PLATFORM_Y and platform_x < dot_x < platform_x + PLATFORM_WIDTH:
        dot_y = PLATFORM_Y - DOT_RADIUS
        dot_velocity_y = 0

    # Prevent the dot from going off the screen horizontally
    if dot_x - DOT_RADIUS < 0:
        dot_x = DOT_RADIUS
    if dot_x + DOT_RADIUS > SCREEN_WIDTH:
        dot_x = SCREEN_WIDTH - DOT_RADIUS

    # Collision detection with the block
    dot_rect = pygame.Rect(dot_x - DOT_RADIUS, dot_y - DOT_RADIUS, DOT_RADIUS * 2, DOT_RADIUS * 2)
    block_rect = pygame.Rect(BLOCK_X, BLOCK_Y, BLOCK_WIDTH, BLOCK_HEIGHT)
    if dot_rect.colliderect(block_rect):
        running = False

    # Fill the screen with a color (e.g., white)
    screen.fill((255, 255, 255))

    # Draw the platform
    pygame.draw.rect(screen, PLATFORM_COLOR, (platform_x, PLATFORM_Y, PLATFORM_WIDTH, PLATFORM_HEIGHT))

    # Draw the block
    pygame.draw.rect(screen, BLOCK_COLOR, (BLOCK_X, BLOCK_Y, BLOCK_WIDTH, BLOCK_HEIGHT))

    # Draw Block Two
    pygame.draw.rect(screen, BLOCK2_COLOR, (BLOCK2_X, BLOCK2_Y, BLOCK2_WIDTH, BLOCK2_HEIGHT))

    # Draw the dot
    pygame.draw.circle(screen, DOT_COLOR, (dot_x, dot_y), DOT_RADIUS)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Clean up
pygame.quit()
sys.exit()

