import pygame
import math
from Body import Planet, Sun

pygame.init()

WIDTH, HEIGHT = 600, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

WHITE = (255, 255, 255)


def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        #WINDOW.fill(WHITE)
        #pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

if __name__ == "__main__":
    main()