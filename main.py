import pygame
import math
from Body import Planet, Sun

pygame.init()

WIDTH, HEIGHT = 800, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (80, 120, 255)
RED = (255, 39, 50)


def main():
    run = True
    clock = pygame.time.Clock()

    sun = Sun(0, 0, 23, YELLOW, 1.98892 * 10**30)

    earth = Planet(-1 * Planet.AU, 0, 12, BLUE, 5.9742 * 10**24)

    mars = Planet(-1.524 * Planet.AU, 0, 8, RED, 6.39 * 10**23)

    planets = [earth, mars]

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