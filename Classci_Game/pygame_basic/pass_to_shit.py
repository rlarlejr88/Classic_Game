import pygame
import random

pygame.init() #reset

#size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption( "Pass to shit!" )

clock = pygame.time.Clock()

background =  pygame.image.load("C:/Users/kimkd/Desktop/Classci_Game/pygame_basic/img/background.png")

character = pygame.image.load("C:/Users/kimkd/Desktop/Classci_Game/pygame_basic/img/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height 


to_x = 0
character_speed = 10

shit = pygame.image.load("C:\\Users\\kimkd\\Desktop\\Classci_Game\\pygame_basic\\img\\enemy.png")
shit_size = shit.get_rect().size
shit_width = shit_size[0]
shit_height = shit_size[1]
shit_x_pos = random.randint(0, screen_width - shit_width)
shit_y_pos = 0 
shit_speed = 5

running = True
while running:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0


    character_x_pos += to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width  

    shit_y_pos += shit_speed

    if shit_y_pos > screen_height:
        shit_y_pos = 0
        shit_x_pos = random.randint(0, screen_width - shit_width)

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    shit_rect = shit.get_rect()
    shit_rect.left = shit_x_pos
    shit_rect.top = shit_y_pos

    if character_rect.colliderect(shit_rect):
        print("OMG")
        running = False


    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(shit, (shit_x_pos, shit_y_pos))
    pygame.display.update()


pygame.uqit()
