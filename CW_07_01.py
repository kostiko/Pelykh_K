# # import pygame

# # pygame.init()

# # DISPLAY_WIDTH = 500
# # DISPLAY_HEIGHT =400
# # WHITE = (255,255,255)
# # PURPLE = (128,0,128)

# # gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

# # pygame.display.set_caption('My first game')

# # clock = pygame.time.Clock()


# # # Loop until the user clicks the close button.
# # done = False
# # # Used to manage how fast the screen updates

# # # -------- Main Program Loop -----------
# # while not done:
# #     # --- Main event loop
    
# #     # for event in pygame.event.get():  # User did something
# #     #     if event.type == pygame.QUIT:  # If user clicked close
# #     #         done = True  # Flag that we are done so we exit this loop

# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             print("User asked to quit.")
# #         elif event.type == pygame.KEYDOWN:
# #             print("User pressed a key.")
# #         elif event.type == pygame.KEYUP:
# #             print("User let go of a key.")
# #         elif event.type == pygame.MOUSEBUTTONDOWN:
# #             print("User pressed a mouse button")


# #     # --- Game logic should go here
# #     # --- Drawing code should go here
# #     # First, clear the screen to white. Don't put other drawing commands
# #     # above this, or they will be erased with this command.
# #     gameDisplay.fill(PURPLE)
# #     # --- Go ahead and update the screen with what we've drawn.
# #     pygame.display.update()
# #     # --- Limit to 60 frames per second
# #     clock.tick(60)
# #----------------------------------------------------------------------------------

# # Liubov Koliasa, [21.02.20 18:37]
# import pygame
# pygame.init()
# screen = pygame.display.set_mode((500,500))
# pygame.display.set_caption("Draw primitives")
# clock = pygame.time.Clock()
# WHITE=(255,255,255)
# BLACK = (0, 0, 0)
# GRAY = (125, 125, 125)
# LIGHT_BLUE = (64, 128, 255)
# GREEN = (0, 200, 64)
# YELLOW = (225, 225, 0)
# PINK = (230, 50, 230)
# PI = 3.14

# done = False
# clock = pygame.time.Clock()

# while not done:
#     for event in pygame.event.get(): 
#         if event.type == pygame.QUIT:
#             done=True
    
    
#     # #pygame.draw.line(screen, (255,255,255), [10, 30], [290, 15], 3)
#     # pygame.draw.line(screen, WHITE, [10, 30], [290, 15], 3)
#     # pygame.draw.line(screen, WHITE, [10, 50], [290, 35])
    
#     # #aaline згладжена лінія, товщина в цьому
#     # # випадку не задається
#     # pygame.draw.aaline(screen, WHITE, [10, 70], [290, 55])
   
#    #Liubov Koliasa, [21.02.20 18:40]
#     #функції lines і aalines малюють ламані
#     # лінії, а параметр Ttue означає замкнути ламані,
#     # False не замикати
#     # 
#     # pygame.draw.lines(screen, WHITE, True, [[10, 10], [140, 70], [280, 20]], 2)
#     # pygame.draw.aalines(screen, WHITE, False, [[10, 100], [140, 170], [280, 110]])

# # 
#     # pygame.draw.polygon(screen, WHITE, [[150, 10], [180, 50], [90, 90], [30, 30]],8)
#     # #pygame.draw.polygon(screen, WHITE, [[250, 110], [280, 150], [190, 190], [130, 130]])
#     # pygame.draw.aalines(screen, WHITE, True, [[250, 110], [280, 150], [190, 190], [130, 130]])

# #Liubov Koliasa, [21.02.20 18:43]
#     # r1 = pygame.Rect((150, 20, 100, 75))
 
#     # pygame.draw.rect(screen, WHITE, (20, 20, 100, 75))
#     # pygame.draw.rect(screen, YELLOW, r1, 8)

# #Liubov Koliasa, [21.02.20 18:46]
# # передається прямокутна область, в якій промальовується еліпс

#     #pygame.draw.ellipse(screen, GREEN, (10, 50, 280, 100))


# #
# # (100, 100) координати центра
#     # 50 - радіус

#     # pygame.draw.circle(screen, YELLOW, (100, 100), 50,5)
#     # pygame.draw.circle(screen, PINK, (200, 100), 50)

# #Liubov Koliasa, [21.02.20 18:48]
#     # pygame.draw.arc(screen, WHITE, (10, 50, 280, 100), 0, PI)
#     # pygame.draw.arc(screen, PINK, (50, 30, 200, 150), PI, 2*PI, 3)

#     pygame.display.update()

#-----------------------------------------------------------------------------------------------------------------


# #pylint: disable=C0321 
# import pygame
# pygame.init()
# screen = pygame.display.set_mode((500,500))
# pygame.display.set_caption("My first game")
# #clock = pygame.time.Clock()

# done = False
# clock = pygame.time.Clock()

# while not done:
#     for event in pygame.event.get(): 
#         if event.type == pygame.QUIT:
#             done=True
    
#     pygame.draw.rect(screen, (255,0,0), [55, 50, 80, 55])
    
    
#     pygame.display.update()
#   #clock.tick(60)
#----------------------------------------------------------------------------------------------------------

# import pygame
# pygame.init()
# screen = pygame.display.set_mode((500,500))
# pygame.display.set_caption("My first game")
# #clock = pygame.time.Clock()

# x=50
# y=50
# width=40
# height=60
# vol=5


# run = True
# clock = pygame.time.Clock()

# while run:
#     pygame.time.delay(100)
    
#     for event in pygame.event.get(): 
#         if event.type == pygame.QUIT:
#             run=False
    
#     keys=pygame.key.get_pressed()
    
#     if keys[pygame.K_LEFT] and x>vol:
#         x=x-vol
#         # if x<0:
#         #     break
#     if keys[pygame.K_RIGHT] and x<460:
#         x=x+vol
#     if keys[pygame.K_UP] and y>vol:
#         y=y-vol
#     if keys[pygame.K_DOWN]and y<440:
#         y=y+vol

#     screen.fill((0,0,0)) #перемальовуємо екран, щоб не було trace
#     #if 0<x<440 and 0<y<500:
#     pygame.draw.rect(screen, (255,0,0), [x, y, width, height])
#     pygame.display.update()
#   #clock.tick(60)
#----------------------------------------------------------------------------------------------------------------
# Liubov Koliasa, [21.02.20 19:40]
# fly


import pygame

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])
 
# This sets the name of the window
pygame.display.set_caption('Mario')
 
clock = pygame.time.Clock()

#обновляємо екран 
pygame.display.update()
 
# Set positions of graphics
background_position = [0, 0]
 
# Load and set up graphics.
#background_image = pygame.image.load("saturn_family1.jpg").convert()
player_image = pygame.image.load("mario_1.png").convert()

#Якщо в зображення не має прозорого слою, то щоб його встановити,
#необхідно використати метод set_colorkey() класу Surface:
player_image.set_colorkey(BLACK)
 
done = False
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True            
 
    
# Get the current mouse position. This returns the position
    # as a list of two numbers.
#повертає поточну позицію мишки на екрані
    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]
 
    # Copy image to screen:
#копіює картинку на екран
    screen.blit(player_image, [x, y])
 
#обновляємо екран
    pygame.display.flip()
    screen.fill((0,0,0))
 
    clock.tick(60)


pygame.quit()