import pygame
import sys

fps_clock = pygame.time.Clock()
FPS = 30
pygame.display.set_caption("Stray Cats")

first_rect = pygame.Rect(100, 200, 50, 25)

rect_speed = 2

rect_color = []


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.init()

first_rect = pygame.Rect(100, 200, 50, 25)

# game events
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
        Y_vel -= 7
    Y_vel /= 1.3
    Y_vel += 2
    first_rect.y += Y_vel

    pygame.display.flip()
    fps_clock.tick(FPS)