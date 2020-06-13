import pygame
pygame.init()

screen_width = 1000
screen_length = 1000

win = pygame.display.set_mode((screen_length,screen_width))
pygame.display.set_caption("Game")

character = pygame.image.load('Eton.png')

x = 50
y = 425
width = 64
height = 64
velocity = 15
left = False
right = False

clock = pygame.time.Clock()

def redraw_window():
    win.fill((255,255,255))
    if left == True:
        win.blit(character,(x,y))
    if right == True:
        win.blit(character,(x,y))
        
    pygame.display.update()

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT] and x > velocity:
        x -= velocity
        left = True
        right = False
    elif keys_pressed[pygame.K_RIGHT] and x < (screen_width - width - velocity):
        x += velocity
        left = False
        right = True
    else:
        right = False
        left = False

    if keys_pressed[pygame.K_UP] and y > velocity:
        y -= velocity
    if keys_pressed[pygame.K_DOWN] and y < 500 - height - velocity:
        y += velocity
    redraw_window()

pygame.quit()
