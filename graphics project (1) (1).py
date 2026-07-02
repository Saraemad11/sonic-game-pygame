import pygame
import random

# =========================================
# INIT
# =========================================
pygame.init()
pygame.mixer.init()

# =========================================
# SCREEN
# =========================================
WIDTH = 900
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sonic Game")

clock = pygame.time.Clock()

# =========================================
# LOAD IMAGES
# =========================================
background = pygame.image.load(r"C:\Users\AL-MOSTAFA\Downloads\background.jpg.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

player_img = pygame.image.load(r"C:\Users\AL-MOSTAFA\Downloads\player.png.png")
player_img = pygame.transform.scale(player_img, (80, 80))

obstacle_img = pygame.image.load(r"C:\Users\AL-MOSTAFA\Downloads\obstcle.png")
obstacle_img = pygame.transform.scale(obstacle_img, (60, 60))

coin_img = pygame.image.load(r"C:\Users\AL-MOSTAFA\Downloads\coin.png.png")
coin_img = pygame.transform.scale(coin_img, (40, 40))

# =========================================
# LOAD SOUNDS
# =========================================
jump_sound = pygame.mixer.Sound(r"C:\Users\AL-MOSTAFA\Downloads\jump.wav.mp3")

pygame.mixer.music.load(r"C:\Users\AL-MOSTAFA\Downloads\music.mp3.mp3")
pygame.mixer.music.play(-1)

# =========================================
# PLAYER
# =========================================
player_x = 100
player_y = 350

player_width = 80
player_height = 80

velocity_y = 0
gravity = 1
jump_power = -18

is_jumping = False

# =========================================
# OBSTACLE
# =========================================
obstacle_x = WIDTH
obstacle_y = 370

obstacle_speed = 8

# =========================================
# COIN
# =========================================
coin_x = random.randint(WIDTH, WIDTH + 400)
coin_y = random.randint(200, 350)

coin_speed = 8

# =========================================
# SCORE
# =========================================
score = 0

font = pygame.font.SysFont("Arial", 35)

# =========================================
# GAME LOOP
# =========================================
running = True

while running:

    clock.tick(60)

    # =====================================
    # EVENTS
    # =====================================
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # JUMP
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                velocity_y = jump_power
                is_jumping = True
                jump_sound.play()

    # =====================================
    # GRAVITY
    # =====================================
    velocity_y += gravity
    player_y += velocity_y

    if player_y >= 350:
        player_y = 350
        is_jumping = False

    # =====================================
    # MOVE OBSTACLE
    # =====================================
    obstacle_x -= obstacle_speed

    if obstacle_x < -60:
        obstacle_x = WIDTH + random.randint(0, 300)

    # =====================================
    # MOVE COIN
    # =====================================
    coin_x -= coin_speed

    if coin_x < -40:
        coin_x = random.randint(WIDTH, WIDTH + 400)
        coin_y = random.randint(200, 350)

    # =====================================
    # RECTANGLES
    # =====================================
    player_rect = pygame.Rect(
        player_x,
        player_y,
        player_width,
        player_height
    )

    obstacle_rect = pygame.Rect(
        obstacle_x,
        obstacle_y,
        60,
        60
    )

    coin_rect = pygame.Rect(
        coin_x,
        coin_y,
        40,
        40
    )

    # =====================================
    # COLLISION WITH OBSTACLE
    # =====================================
    if player_rect.colliderect(obstacle_rect):

        game_over_text = font.render(
            "GAME OVER",
            True,
            (255, 0, 0)
        )

        screen.blit(game_over_text, (330, 220))
        pygame.display.update()

        pygame.time.delay(3000)

        running = False

    # =====================================
    # COLLECT COIN
    # =====================================
    if player_rect.colliderect(coin_rect):
        score += 1

        coin_x = random.randint(WIDTH, WIDTH + 400)
        coin_y = random.randint(200, 350)

    # =====================================
    # DRAW
    # =====================================
    screen.blit(background, (0, 0))

    screen.blit(player_img, (player_x, player_y))

    screen.blit(obstacle_img, (obstacle_x, obstacle_y))

    screen.blit(coin_img, (coin_x, coin_y))

    # SCORE TEXT
    score_text = font.render(
        f"Score: {score}",
        True,
        (255, 255, 255)
    )

    screen.blit(score_text, (20, 20))

    pygame.display.update()

pygame.quit()