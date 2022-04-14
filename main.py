import pygame

import random
import math

from star import Star
import config as cfg

pygame.init()

WIN = pygame.display.set_mode((cfg.WIDTH, cfg.HEIGHT))
pygame.display.set_caption("Planet Simulation")


def main():
    run = True
    clock = pygame.time.Clock()

    galaxy = []

    for i in range(cfg.STARS_NUMBER):
        x, y = random_points_circle(cfg.GALAXY_SIZE / 2)
        star = Star(x, random.random() - 0.5, y, random.random() - 0.5, (255, 255, 255))
        galaxy.append(star)

    while run:
        clock.tick(60)
        WIN.fill(cfg.BG_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for star in galaxy:
            star.update_position(galaxy)
            star.draw(WIN)

        pygame.display.update()

    pygame.quit()


def random_points_circle(radius):
    u = random.random()
    radius *= math.sqrt(u)
    theta = random.uniform(0., 2 * math.pi)
    x = radius * math.cos(theta)
    y = radius * math.sin(theta)
    return x, y


main()
