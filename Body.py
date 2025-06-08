import pygame
import math


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

    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        F = self.G * self.mass * other.mass / distance**2
        theta = math.atan2(distance_y, distance_x)
        F_x = F * math.cos(theta)
        F_y = F * math.sin(theta)
        return F_x, F_y

    def update_position(self, bodies):
        net_F_x = net_F_y = 0
        for body in bodies:
            if self == body:
                continue

            F_x, F_y = self.attraction(body)
            net_F_x += F_x
            net_F_y += F_y

        self.v_x += net_F_x / self.mass * self.TIMESTEP
        self.v_y += net_F_y / self.mass * self.TIMESTEP

        self.x += self.v_x * self.TIMESTEP
        self.y += self.v_y * self.TIMESTEP
        self.orbit.append((self.x, self.y))


class Planet(Body):
    def __init__(self, x, y, radius, colour, mass):
        super().__init__(x, y, radius, colour, mass)
        self.distance_from_sun = 0

    def attraction(self, other):
        F_x, F_y = super().attraction(other)

        if isinstance(other, Sun):
            distance_x = other.x - self.x
            distance_y = other.y - self.y
            self.distance_from_sun = math.sqrt(distance_x ** 2 + distance_y ** 2)

        return F_x, F_y


class Sun(Body):
    def __init__(self, x, y, radius, colour, mass):
        super().__init__(x, y, radius, colour, mass)