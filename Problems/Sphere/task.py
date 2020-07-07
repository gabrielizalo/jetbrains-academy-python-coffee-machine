class Sphere:
    PI = 3.1415

    def __init__(self, radius):
        self.radius = radius
        self.volume = self.calculate_volume()

    def calculate_volume(self):
        return pow(self.radius, 3) * Sphere.PI * (4 / 3)
