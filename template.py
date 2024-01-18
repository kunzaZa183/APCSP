import pygame

pygame.init()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            c = pygame.key.name(event.key)
            if c == "enter":
                break
            else:
                print(c)
