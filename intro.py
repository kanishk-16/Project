import pygame
from sys import exit

pygame.init()
screen= pygame.display.set_mode((800,400))
pygame.display.set_caption("Flappy Bird")
clock =  pygame.time.Clock()

icon_path=r"C:\Users\kanis\OneDrive\Desktop\Python-Class\Project\graphics\pngegg.png"
icon_image= pygame.image.load(icon_path)
pygame.display.set_icon(icon_image)


test_font = pygame.font.Font('Project/fonts/Pixeltype.ttf',50)

sky_surface = pygame.image.load('Project/graphics/Sky.png').convert()
ground_surface = pygame.image.load('Project/graphics/ground.png').convert()
text_surface = test_font.render('Flappy Bird',False,'Red')

bird_surface = pygame.image.load('Project/graphics/bird1.png').convert_alpha()
bird_x_pos=100

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(320,50))
    bird_x_pos += 8 
    if bird_x_pos > 800: bird_x_pos=0
    
    screen.blit(bird_surface,(bird_x_pos,200))
    
    pygame.display.update()
    clock.tick(60)        
