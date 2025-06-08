import pygame
import math
from Body import Planet, Sun

pygame.init()

WIDTH, HEIGHT = 600, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)


def main():
    run = True
    clock = pygame.time.Clock()

    sun = Sun(0, 0, 23, YELLOW, 1.98892 * 10 ** 30)

    planets = []

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        sun.draw(WINDOW, HEIGHT, WIDTH)
        for planet in planets:
            planet.draw(WINDOW, HEIGHT, WIDTH)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()