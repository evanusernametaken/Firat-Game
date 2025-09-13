import pygame
import sys
import math
import random

Menu = "Main"
fps_clock = pygame.time.Clock()
FPS = 30
pygame.display.set_caption("Stray Cats")
Cat_Sprites = [pygame.image.load("assets/Betli Fly 1 (Larger).png"), pygame.image.load("assets/Betli Fly 2 (Larger).png"), pygame.image.load("assets/Betli Fly Up 1 (Larger).png"), pygame.image.load("assets/Betli Fly Up 2 (Larger).png"), pygame.image.load("assets/Betli Hurt (Larger).png")]
Menu_Assets = [pygame.image.load("assets/start button.png"), pygame.image.load("assets/name title.png"), pygame.image.load("assets/press any button to start.png")]
rect_speed = 2
first_rect = pygame.Rect(100, 200, 44, 35)
Cat_Rect = Cat_Sprites[0].get_rect()
Cat_Location_X = 0
Cat_Location_Y = 0
# first_rect = pygame.Rect(100, 200, 50, 25)
Rotation = 0
Current_Rotation = 0
# Variables
rect_speed = 2
rect_color = []
Start_button_rect = Menu_Assets[0].get_rect()
sky = pygame.image.load("assets/Sky Clouds.png")
floor = pygame.image.load("assets/Floor Grass.png")
scratch_post = pygame.image.load("assets/scratching post part 2.png")


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.init()

# first_rect = pygame.Rect(100, 200, 44, 35)
floor_x = 0
floor_width = floor.get_width()
floor_2x = floor_width
grass_floor = 500
grass_width = 1067

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


scratch_post_rect = scratch_post.get_rect()
scratch_post_rect.topleft = [grass_floor, 429]

scratch_post_rect_2 = pygame.Rect(scratch_post_rect.left, scratch_post_rect.top, scratch_post_rect.width, scratch_post_rect.height)
scratch_post_rect_2.topleft = [grass_floor + 100, 429]

scratch_post_rect

scratch_post_rects = [scratch_post_rect, scratch_post_rect_2]
Rotation = 0
Current_Rotation = 0
copy_death_cat = Cat_Sprites[4]
while True:
    screen.fill([0, 255, 0])
    frames += 1
    # if first_rect.x >= 1200 - first_rect.w:
    #     rect_speed = rect_speed * -1
    # if first_rect.x <= 0:
    #     rect_speed = rect_speed * -1

    # first_rect.x = first_rect.x + rect_speed
    screen.blit(sky, [0,0])
    screen.blit(floor, [floor_x, 0])
    screen.blit(floor, [floor_2x, 0])

    for scratch_post_rect in scratch_post_rects:
        scratch_post_rect.x = scratch_post_rect.x - 4
        screen.blit(scratch_post, scratch_post_rect)
    
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
    Cat_Rect.top = Cat_Location_Y
    Cat_Rect.left = Cat_Location_X
    if animation == 1: 
        screen.blit(Cat_Sprites[round((frames%5)/5)], Cat_Rect)
    elif animation == 2: 
        screen.blit(Cat_Sprites[round((frames%5)/5) + 2], Cat_Rect)
    elif animation == 3: 
        screen.blit(copy_death_cat, Cat_Rect)
    # pygame.draw.rect(screen, [255, 255, 255], first_rect)
    if Menu == "Main":
        screen.blit(Menu_Assets[1], (300, 100, 0, 0))
        Start_button_rect.y = math.sin(frames*(math.pi/60))*10 + 300
        Start_button_rect.x = 300
        screen.blit(Menu_Assets[0], Start_button_rect)
    elif Menu == "Start":
        screen.blit(Menu_Assets[2], (300, 200, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Start_button_rect.collidepoint(pygame.mouse.get_pos()):
                Menu = "Start"
        if event.type == pygame.KEYDOWN:
            if Menu == "Start": Menu = "MainGame"
            else: pass
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
    if Menu == "Start" or Menu == "Main":
        Cat_Location_X = 150
        Cat_Location_Y = (math.sin(frames * (math.pi/90))*50)+200
    elif Menu == "MainGame":
        if Cat_Location_Y > screen_height - 140:
            if Menu != "Death":
                    Menu = "Death"
                    Y_vel = -40
        if up_is_pressed:
            frames += 1
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
        if Cat_Location_Y < 10:
            Y_vel = 5
        if Cat_Location_X < 10:
            X_vel = 5
        elif screen_width - 100 < Cat_Location_X:
            X_vel = -5
        #check if cat hit post
        for scratch_post_rect in scratch_post_rects:
            if scratch_post_rect.colliderect(Cat_Rect):
                if Menu != "Death":
                    Menu = "Death"
                    Y_vel = -40



    elif Menu == "Death":
        if Cat_Location_Y < screen_height: Rotation -= 20
        else: Menu = "DeathScreen"
        animation = 3
        Y_vel /= 1.1
        Y_vel += 1
        Cat_Location_Y += Y_vel
    elif Menu == "Death Screen":
        pygame.font.SysFont("impact", 32).pygame.font.SysFont("impact", 32)
    if Rotation != Current_Rotation:
        copy_death_cat = pygame.transform.rotate(Cat_Sprites[4], Rotation)
        Current_Rotation = Rotation
    pygame.display.flip()
    fps_clock.tick(FPS)