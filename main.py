import pygame
from Body import Planet, Sun

pygame.init()

WIDTH, HEIGHT = 800, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

YELLOW = (255, 255, 0)
BLUE = (60, 100, 255)
RED = (245, 49, 60)
DARK_GREY = (80, 78, 81)
CREAM = (255, 253, 208)


def main():
    run = True
    clock = pygame.time.Clock()

    sun = Sun(0, 0, 23, YELLOW, 1.98892 * 10**30)
    earth = Planet(Planet.AU, 0, 12, BLUE, 5.9742 * 10**24)
    mars = Planet(1.524 * Planet.AU, 0, 8, RED, 6.39 * 10**23)
    mercury = Planet(0.387 * Planet.AU, 0,  6, DARK_GREY, 0.330 * 10**24)
    venus = Planet(0.723 * Planet.AU, 0, 11, CREAM, 4.8685 * 10**24)

    bodies = [sun, mercury, venus, earth, mars]

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for body in bodies:
            body.draw(WINDOW, HEIGHT, WIDTH)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()