import pygame

pygame.init()

width = 800
height = 500

screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 255, 255))
    pygame.display.update()
    
    clock.tick(60)

pygame.quit()