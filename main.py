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

    for i in range(10):
        star = Star((random() * 400)-200, (random()*2)-1, (random() * 400)-200, (random()*2)-1, cfg.WHITE)
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
