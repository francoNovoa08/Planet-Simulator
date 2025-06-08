class Planet:
    AU = 149597870.7
    G = 6.67428e-11
    SCALE = 250 / AU # 1 AU = 100 px
    TIMESTEP = 3600 * 24 # 1 day

    def __init__(self, x, y, radius, colour, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour
        self.mass = mass

        self.orbit = []

        self.sun = False
        self.distance_from_sun = 0

        self.v_x = 0
        self.v_y = 0