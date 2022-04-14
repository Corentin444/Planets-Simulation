import pygame
import config as cfg

pygame.init()


class Star:

    def __init__(self, x_position, x_speed, y_position, y_speed, color):
        self.x_position = x_position
        self.x_speed = x_speed
        self.x_acceleration = 0

        self.y_position = y_position
        self.y_speed = y_speed
        self.y_acceleration = 0

        self.color = color

    def draw(self, win):
        x = self.x_position + cfg.WIDTH / 2
        y = self.y_position + cfg.HEIGHT / 2

        pygame.draw.circle(win, self.color, (x, y), 1)
        # win.set_at((self.x_position, self.y_position), self.color)

    def update_position(self, galaxy):
        self.x_acceleration = 0
        for star in galaxy:
            if star != self:
                f = 1 / (((self.x_position - star.x_position) ** 2) + cfg.SMOOTHING)
                if (self.x_position - star.x_position) < 0:
                    self.x_acceleration -= f
                else:
                    self.x_acceleration += f
        self.x_speed += self.x_acceleration * cfg.TIMESTEP
        self.x_position += self.x_speed * cfg.TIMESTEP

        self.y_acceleration = 0
        for star in galaxy:
            if star != self:
                f = 1 / (((self.y_position - star.y_position) ** 2) + cfg.SMOOTHING)
                if (self.y_position - star.y_position) < 0:
                    self.y_acceleration -= f
                else:
                    self.y_acceleration += f
        self.y_speed += self.y_acceleration * cfg.TIMESTEP
        self.y_position += self.y_speed * cfg.TIMESTEP

        # self.debug()

    def debug(self):
        print("x_position = ", self.x_position, " | y_position = ", self.y_position)
        print("x_speed = ", self.x_speed, " | y_speed = ", self.y_speed)
        print("x_acceleration = ", self.x_acceleration, " | y_acceleration = ", self.y_acceleration)
        print()
