import pygame
import sys

fps_clock = pygame.time.Clock()
FPS = 30
pygame.display.set_caption("Stray Cats")
first_rect = pygame.Rect(100, 200, 50, 25)
Cat_Sprites = [pygame.image.load("assets/Betli Fly 1 (Larger).png"), pygame.image.load("assets/Betli Fly 2 (Larger).png"), pygame.image.load("assets/Betli Fly Up 1 (Larger).png"), pygame.image.load("assets/Betli Fly Up 2 (Larger).png"), pygame.image.load("assets/Betli Hurt (Larger).png")]
rect_speed = 2
first_rect = pygame.Rect(100, 200, 44, 35)
Cat_Rect = Cat_Sprites[0].get_rect()
Cat_Location_X = 0
Cat_Location_Y = 0
rect_color = []

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.init()


# game events
Y_vel = 0
X_vel = 0
up_is_pressed = False
right_is_pressed = False
game_is_running = True
left_is_pressed = False
x_acceleration = 0.5
y_acceleration = 2
animation = 1
frames = 0
while True:
    frames += 1
    screen.fill([0, 255, 0])

    # if first_rect.x >= 1200 - first_rect.w:
    #     rect_speed = rect_speed * -1
    # if first_rect.x <= 0:
    #     rect_speed = rect_speed * -1

    # first_rect.x = first_rect.x + rect_speed
    Cat_Rect.top = Cat_Location_Y
    Cat_Rect.left = Cat_Location_X
    if animation == 1: screen.blit(Cat_Sprites[round((frames%5)/5)], Cat_Rect)
    elif animation == 2: screen.blit(Cat_Sprites[round((frames%5)/5) + 2], Cat_Rect)
    pygame.draw.rect(screen, [255, 255, 255], first_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                up_is_pressed = True
            if event.key == pygame.K_RIGHT:
                right_is_pressed = True
            if event.key == pygame.K_LEFT:
                left_is_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                up_is_pressed = False
            if event.key == pygame.K_RIGHT:
                right_is_pressed = False
            if event.key == pygame.K_LEFT:
                left_is_pressed = False
    if up_is_pressed:
        Y_vel -= 2
        animation = 2
    else:
        animation = 1
    if right_is_pressed:
        X_vel += 0.5
    if left_is_pressed:
        X_vel -= 0.5
    Y_vel /= 1.1
    X_vel /= 1.1
    Y_vel += 1
    X_vel -= 0.2
    Cat_Location_X += X_vel
    Cat_Location_Y += Y_vel

    pygame.display.flip()
    fps_clock.tick(FPS)