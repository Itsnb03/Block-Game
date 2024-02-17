import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Player
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size - 10
player_speed = 5

# Blocks
block_width = 50
block_height = 50
block_speed = 2
block_list = []

# Create a window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Block Game")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Functions
def draw_player(x, y):
    pygame.draw.rect(screen, WHITE, [x, y, player_size, player_size])

def draw_blocks(blocks):
    for block in blocks:
        pygame.draw.rect(screen, WHITE, block)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    # Move blocks
    for block in block_list:
        block[1] += block_speed

    # Spawn new blocks
    if random.randint(1, 100) < 5:
        block_x = random.randint(0, WIDTH - block_width)
        block_y = 0
        block_list.append([block_x, block_y, block_width, block_height])

    # Check collisions with blocks
    for block in block_list:
        if (
            player_x < block[0] + block[2]
            and player_x + player_size > block[0]
            and player_y < block[1] + block[3]
            and player_y + player_size > block[1]
        ):
            print("Game Over!")
            running = False

    # Remove off-screen blocks
    block_list = [block for block in block_list if block[1] < HEIGHT]

    # Clear the screen
    screen.fill(BLACK)

    # Draw player and blocks
    draw_player(player_x, player_y)
    draw_blocks(block_list)

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
