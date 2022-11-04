# code
import pygame
import sys


class Picture:
    def __init__(self, screen, image_address):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load(image_address)
        self.rect = self.image.get_rect()
        self.x = float(self.rect.x)

    def draw(self):
        self.screen.blit(self.image, self.rect)


pygame.init()

while True:
    screen = pygame.display.set_mode((400, 600))
    screen.fill((0, 0, 255))

    ship = Picture(screen, "ship.bmp")
    ship.draw()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.rect.x = ship.rect.x + 1
            elif event.key == pygame.K_LEFT:
                ship.rect.y = ship.rect.y + 1
            elif event.key == pygame.K_q:
                sys.exit()


