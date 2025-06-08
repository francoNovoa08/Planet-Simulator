import pygame


class Body:
    AU = 149597870.7
    G = 6.67428e-11
    SCALE = 200 / AU
    TIMESTEP = 3600 * 24

    def __init__(self, x, y, radius, colour, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour
        self.mass = mass
        self.orbit = []
        self.v_x = 0
        self.v_y = 0

    def draw(self, window, height, width):
        x = self.x * self.SCALE + width / 2
        y = self.y * self.SCALE + height / 2
        pygame.draw.circle(window, self.colour, (x, y), self.radius)


class Planet(Body):
    def __init__(self, x, y, radius, colour, mass):
        super().__init__(x, y, radius, colour, mass)
        self.distance_from_sun = 0


class Sun(Body):
    def __init__(self, x, y, radius, colour, mass):
        super().__init__(x, y, radius, colour, mass)