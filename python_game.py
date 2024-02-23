import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()
ground = pygame.image.load("C:\\Users\\Jahkai\\Desktop\\ground.png")
sky = pygame.image.load("C:\\Users\\Jahkai\\Desktop\\sky.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(sky, (0,0))
    screen.blit(ground, (0, 300))

    pygame.display.update()
    clock.tick(60)
