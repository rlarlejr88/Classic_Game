import pygame

pygame.init() #reset

#size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption( "Classic Game" )

background = pygame.image.load("C:\\Users\\kimkd\\Desktop\\Classci_Game\\pygame_basic\\background.png")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # screen.fill((0,0,255))
    screen.blit(background, (0,0))
    pygame.display.update()
pygame.uqit()
