import pygame
import sys
import math
import random
import json
Distance = 0
Menu = "Main"
name = "None"
fps_clock = pygame.time.Clock()
FPS = 30
pygame.display.set_caption("Stray Cats")
Cat_Sprites = [pygame.image.load("assets/Betli Fly 1 (Larger).png"), pygame.image.load("assets/Betli Fly 2 (Larger).png"), pygame.image.load("assets/Betli Fly Up 1 (Larger).png"), pygame.image.load("assets/Betli Fly Up 2 (Larger).png"), pygame.image.load("assets/Betli Hurt (Larger).png")]
Menu_Assets = [pygame.image.load("assets/start button.png"), pygame.image.load("assets/name title.png"), pygame.image.load("assets/press any button to start.png"), pygame.image.load("assets/GO2.png"), pygame.image.load("assets/name credits.png")]
Obstikle_Sprites = [pygame.image.load("assets/scratching post part 2.png"), pygame.image.load("assets/YarnBall2.png"), pygame.image.load("assets/Pigsus.png"), pygame.image.load("assets/PigsusTelegraph.png")]
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
sky = pygame.image.load("assets/Sky Clouds 2.png")
floor = pygame.image.load("assets/Floor Grass.png")
Level = 1
scores = []
with open("scores.json", "r") as score_file:
    scores = json.load(score_file)
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.init()
pygame.font.init()
highscores = [0, "None"]
for i in scores:
    if i[0] > highscores[0]: highscores = i

# first_rect = pygame.Rect(100, 200, 44, 35)
floor_x = 0
floor_width = floor.get_width()
floor_2x = floor_width
grass_floor = 500
grass_width = 1067
sky_x = 0
sky_width = sky.get_width()
sky_2x = sky_width


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


scratch_post_rect = Obstikle_Sprites[0].get_rect()
scratch_post_rect.topleft = [800, 405]
scratch_post_rect_2 = Obstikle_Sprites[1].get_rect()
scratch_post_rect_2.topleft = [800, 0]
pigsus_rect = Obstikle_Sprites[2].get_rect()
pigsus_rect.topleft = [800, 0]
pigsusTelegraph_rect = pygame.Rect(600, 0, 0, 0)
# Really Any Moving Object
scratch_post_rects = []
object_id = []
object_spawned_at = []
Rotation = 0
Current_Rotation = 0
copy_death_cat = Cat_Sprites[4]
while True:
    frames += 1
    
    # if first_rect.x >= 1200 - first_rect.w:
    #     rect_speed = rect_speed * -1
    # if first_rect.x <= 0:
    #     rect_speed = rect_speed * -1

    # first_rect.x = first_rect.x + rect_speed
    screen.blit(sky, [0,0])
    screen.blit(sky, [sky_x,0])
    screen.blit(sky, [sky_2x, 0])
    screen.blit(floor, [floor_x, 0])
    screen.blit(floor, [floor_2x, 0])

    new_scratch_posts = []

    if Menu == "MainGame" or Menu == "Death":
        if Distance < 250:
            if Distance % 60 == 0:
                new_scratch_post_rect = pygame.Rect(scratch_post_rect)
                new_scratch_post_rect.x = random.randint(800, 1000)
                new_scratch_post_rect.y = 405
                scratch_post_rects.append(new_scratch_post_rect)
                object_id.append(1)
                object_spawned_at.append(Distance)
        elif Distance < 500:
            if Distance % 30 == 0:
                new_scratch_post_rect = pygame.Rect(scratch_post_rect)
                new_scratch_post_rect.x = random.randint(800, 1000)
                new_scratch_post_rect.y = 405
                scratch_post_rects.append(new_scratch_post_rect)
                object_id.append(1)
                object_spawned_at.append(Distance)
        elif Distance < 1000:
            if Distance % 60 == 0:
                new_scratch_post_rect = pygame.Rect(scratch_post_rect)
                new_scratch_post_rect.x = random.randint(800, 1000)
                new_scratch_post_rect.y = 405
                scratch_post_rects.append(new_scratch_post_rect)
                object_id.append(1)
                object_spawned_at.append(Distance)
            if Distance % 120 == 23:
                new_scratch_post_rect = pygame.Rect(scratch_post_rect_2)
                new_scratch_post_rect.x = random.randint(800, 1000)
                new_scratch_post_rect.y = 0
                scratch_post_rects.append(new_scratch_post_rect)
                object_id.append(random.randint(2, 3))
                object_spawned_at.append(Distance)
        elif Distance < 2000:
            if Distance % 60 == 0:
                new_scratch_post_rect = pygame.Rect(scratch_post_rect)
                new_scratch_post_rect.x = random.randint(800, 1000)
                new_scratch_post_rect.y = 405
                scratch_post_rects.append(new_scratch_post_rect)
                object_id.append(1)
                object_spawned_at.append(Distance)
            if Distance % 60 == 26:
                new_scratch_post_rect = pygame.Rect(scratch_post_rect_2)
                new_scratch_post_rect.x = random.randint(800, 1000)
                new_scratch_post_rect.y = 0
                scratch_post_rects.append(new_scratch_post_rect)
                object_id.append(random.randint(2, 3))
                object_spawned_at.append(Distance)
        elif 2200 < Distance < 3000:
            if Distance % 30 == 10:
                new_scratch_post_rect = pygame.Rect(pigsusTelegraph_rect)
                new_scratch_post_rect.x = 600
                new_scratch_post_rect.y = random.randint(0, 350)
                scratch_post_rects.append(new_scratch_post_rect)
                object_id.append(6)
                object_spawned_at.append(Distance)
            if Distance % 30 == 0:
                new_scratch_post_rect = pygame.Rect(scratch_post_rect)
                new_scratch_post_rect.x = random.randint(800, 1000)
                new_scratch_post_rect.y = 405
                scratch_post_rects.append(new_scratch_post_rect)
                object_id.append(1)
                object_spawned_at.append(Distance)
        elif 3200 < Distance < 4000:
            if Distance % 30 == 26:
                new_scratch_post_rect = pygame.Rect(scratch_post_rect_2)
                new_scratch_post_rect.x = random.randint(800, 1000)
                new_scratch_post_rect.y = 0
                scratch_post_rects.append(new_scratch_post_rect)
                object_id.append(random.randint(2, 3))
                object_spawned_at.append(Distance)
        elif 4200 < Distance < 5000:
            if Distance % 20 == 10:
                new_scratch_post_rect = pygame.Rect(pigsusTelegraph_rect)
                new_scratch_post_rect.x = 600
                new_scratch_post_rect.y = random.randint(0, 350)
                scratch_post_rects.append(new_scratch_post_rect)
                object_id.append(6)
                object_spawned_at.append(Distance)
            if Distance % 30 == 0:
                new_scratch_post_rect = pygame.Rect(scratch_post_rect)
                new_scratch_post_rect.x = random.randint(800, 1000)
                new_scratch_post_rect.y = 405
                scratch_post_rects.append(new_scratch_post_rect)
                object_id.append(1)
                object_spawned_at.append(Distance)
        elif 5200 < Distance:
            if Distance % 120 == 10:
                new_scratch_post_rect = pygame.Rect(pigsusTelegraph_rect)
                new_scratch_post_rect.x = 600
                new_scratch_post_rect.y = random.randint(0, 350)
                scratch_post_rects.append(new_scratch_post_rect)
                object_id.append(6)
                object_spawned_at.append(Distance)
            if Distance % 60 == 0:
                new_scratch_post_rect = pygame.Rect(scratch_post_rect)
                new_scratch_post_rect.x = random.randint(800, 1000)
                new_scratch_post_rect.y = 405
                scratch_post_rects.append(new_scratch_post_rect)
                object_id.append(1)
                object_spawned_at.append(Distance)
            if Distance % 60 == 26:
                new_scratch_post_rect = pygame.Rect(scratch_post_rect_2)
                new_scratch_post_rect.x = random.randint(800, 1000)
                new_scratch_post_rect.y = 0
                scratch_post_rects.append(new_scratch_post_rect)
                object_id.append(random.randint(2, 3))
                object_spawned_at.append(Distance)
        if Menu == "MainGame": Distance += 1
        

        screen.blit(pygame.font.SysFont("impact", 32).render("Distance: " + str(Distance), False, [0, 0, 0]), (0, 0, 0, 0))
    #     for i in range(len(scratch_post_rects)):
    #         if object_id[i] == 1:
    #             scratch_post_rects[i].x -= 4
    #             screen.blit(Obstikle_Sprites[0], scratch_post_rects[i])
    #             if scratch_post_rects[i].x > -50:
    #                 new_scratch_posts.append(scratch_post_rects[i])
    #                 object_id.append(1)
    #         elif object_id[i] == 2:
    #             scratch_post_rects[i].x -= 4
    #         scratch_post_rects = new_scratch_posts
    #     # if len(scratch_post_rects) < 10:
    #     #      scratch_post_rect = Obstikle_Sprites[0].get_rect()
    #     #      scratch_x = random.randint(300, 500) + scratch_post_rects[-1].x
    #     #      scratch_post_rect.topleft = [scratch_x, 405]
    #     #      scratch_post_rects.append(scratch_post_rect)
    #     #      object_id.append(1)
        loops = len(scratch_post_rects) -1
        while loops >= 0:
            # print(scratch_post_rects[loops])
            if object_id[loops] == 1:
                scratch_post_rects[loops].x -= 4
                screen.blit(Obstikle_Sprites[0], scratch_post_rects[loops])
            if object_id[loops] == 2:
                scratch_post_rects[loops].x -= 4
                
                if abs(scratch_post_rects[loops].x - Cat_Location_X) < 260:
                    screen.blit(Obstikle_Sprites[1], (scratch_post_rects[loops].x + math.sin(Distance*(math.pi/10))*((260-abs(scratch_post_rects[loops].x - Cat_Location_X))/10), scratch_post_rects[loops].y, scratch_post_rects[loops].width, scratch_post_rects[loops].height))
                else:
                    screen.blit(Obstikle_Sprites[1], scratch_post_rects[loops])
                if abs(scratch_post_rects[loops].x - Cat_Location_X) < 160:
                    object_id[loops] = random.randint(4, 5)
            if object_id[loops] == 3:
                scratch_post_rects[loops].x -= 4
                screen.blit(Obstikle_Sprites[1], scratch_post_rects[loops])
            if object_id[loops] == 4:
                scratch_post_rects[loops].y += 20
                scratch_post_rects[loops].x -= 4
                screen.blit(Obstikle_Sprites[1], scratch_post_rects[loops])
            if object_id[loops] == 5:
                scratch_post_rects[loops].y += 6
                scratch_post_rects[loops].x -= 4
                screen.blit(Obstikle_Sprites[1], scratch_post_rects[loops])
            if object_id[loops] == 6:
                screen.blit(Obstikle_Sprites[3], scratch_post_rects[loops])
                if object_spawned_at[loops] + 60 < Distance:
                    scratch_post_rects[loops] = pygame.Rect(scratch_post_rects[loops].x + 200, scratch_post_rects[loops].y, Obstikle_Sprites[2].get_rect().width, Obstikle_Sprites[2].get_rect().height)
                    object_id[loops] = 7
            if object_id[loops] == 7:
                scratch_post_rects[loops].x -= 24
                screen.blit(Obstikle_Sprites[2], scratch_post_rects[loops])
            if scratch_post_rects[loops].x < -100: 
                del scratch_post_rects[loops]
                del object_id[loops]
                del object_spawned_at[loops]
            loops -= 1

    grass_width = grass_width - 4
    grass_floor = grass_floor - 4
    if grass_floor <= -1 * grass_width:
        grass_width = -1 * grass_width
    floor_2x = floor_2x - 4
    floor_x = floor_x - 4
    if floor_x <= -1 * floor_width:
        floor_x = 2 * floor_width + floor_x
    if floor_2x <= -1 * floor_width:
        floor_2x = 2 * floor_width + floor_2x
    
    sky_2x = sky_2x - 1
    sky_x = sky_x - 1
    if sky_x <= -1 * sky_width:
        sky_x = sky_width
    if sky_2x <= -1 * sky_width:
        sky_2x = sky_width
        
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
        screen.blit(Menu_Assets[4], (0, 0, 0, 0))
    elif Menu == "Start":
        screen.blit(Menu_Assets[2], (300, 200, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Start_button_rect.collidepoint(pygame.mouse.get_pos()) and Menu == "Main":
                Menu = "Start"
        if event.type == pygame.KEYDOWN:
            if Menu == "Start": Menu = "MainGame"
            if Menu == "DeathScreen": 
                Menu = "Start"
                animation = 1
                Distance = 0
                scratch_post_rects = []
                object_id = []
                object_spawned_at = []
                Cat_Location_X = 150
                Cat_Location_Y = (math.sin(frames * (math.pi/90))*50)+200
            if event.key == pygame.K_UP  or event.key == pygame.K_SPACE:
                up_is_pressed = True
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                right_is_pressed = True
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                left_is_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                up_is_pressed = False
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                right_is_pressed = False
            if event.key == pygame.K_LEFT  or event.key == pygame.K_a:
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
        else:
            #if name == "None": name = input("What is your name?")
            scores.append([Distance, name])
            with open("scores.json", "w") as score_file:
                json.dump(scores, score_file) 
            Menu = "DeathScreen"
        animation = 3
        Y_vel /= 1.1
        Y_vel += 1
        Cat_Location_Y += Y_vel
    elif Menu == "DeathScreen":
        screen.fill([0, 0, 0])
        if (highscores[0] <= Distance): 
            screen.blit(pygame.font.SysFont("impact", 32).render("New High Score!", False, [255, 255, 255]), (300, 550, 0, 0))
            highscores = [Distance, name]
        screen.blit(pygame.font.SysFont("impact", 32).render("Distance: " + str(Distance), False, [255, 255, 255]), (0, 0, 0, 0))
        screen.blit(pygame.font.SysFont("impact", 32).render("Current Highscore: " + str(str(highscores[0])), False, [255, 255, 255]), (0, 32, 0, 0))
        screen.blit(Menu_Assets[3], (25, 100, 0, 0))
    if Rotation != Current_Rotation:
        copy_death_cat = pygame.transform.rotate(Cat_Sprites[4], Rotation)
        Current_Rotation = Rotation
    pygame.display.flip()
    fps_clock.tick(FPS)