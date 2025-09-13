import pygame
import sys

fps_clock = pygame.time.Clock()
FPS = 30
pygame.display.set_caption("Stray Cats")

first_rect = pygame.Rect(100, 200, 50, 25)

# Variables
rect_speed = 2
rect_color = []

sky = pygame.image.load("assets/Sky Clouds.png")
floor = pygame.image.load("assets/Floor Grass.png")
scratch_post = pygame.image.load("assets/scratching post part 2.png")

grass_floor = 429
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.init()

first_rect = pygame.Rect(100, 200, 50, 25)
floor_x = 0
floor_width = floor.get_width()
floor_2x = floor_width
grass_floor = 500
grass_width = 1067

# Game Events
Y_vel = 0
X_vel = 0
up_is_pressed = False
game_is_running = True
while True:
    screen.fill([0, 255, 0])

    # if first_rect.x >= 1200 - first_rect.w:
    #     rect_speed = rect_speed * -1
    # if first_rect.x <= 0:
    #     rect_speed = rect_speed * -1

    # first_rect.x = first_rect.x + rect_speed
    screen.blit(sky, [0,0])
    screen.blit(floor, [floor_x, 0])
    screen.blit(floor, [floor_2x, 0])
    screen.blit(scratch_post, [grass_floor, 429])
    
    grass_width = grass_width - 4
    grass_floor = grass_floor - 4
    if grass_floor <= -1 * grass_width:
        grass_width = -1 * grass_width
    floor_2x = floor_2x - 4
    floor_x = floor_x - 4
    if floor_x <= -1 * floor_width:
        floor_x = floor_width
    if floor_2x <= -1 * floor_width:
        floor_2x = floor_width
    pygame.draw.rect(screen, [255, 255, 255], first_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                first_rect.x = 600
                rect_speed = abs(rect_speed)
                rect_color = [255, 255, 255]
            if event.key == pygame.K_UP:
                up_is_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                up_is_pressed = False
    print(up_is_pressed)
    if up_is_pressed:
        Y_vel -= 6
    Y_vel /= 1.3
    Y_vel += 1.5
    first_rect.y += Y_vel

    pygame.display.flip()
    fps_clock.tick(FPS)