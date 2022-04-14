from random import random

import pygame

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
        star = Star((random() * cfg.GALAXY_SIZE) - (cfg.GALAXY_SIZE / 2), random() - 0.5,
                    (random() * cfg.GALAXY_SIZE) - (cfg.GALAXY_SIZE / 2), random() - 0.5,
                    (255, 255, 255))
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


main()
