import pygame
import sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((600, 600))


pygame.display.set_caption("Mummy maze !!")

surfaceMap = pygame.transform.scale(
    pygame.image.load("./image/floor.jpg"), (600, 600))


# (0,0) - (60,0) - (120, 0) - (180 , 0) - (240, 0)

playerUp = pygame.image.load("./image/player/move_up.png")
playerDown = pygame.image.load("./image/player/move_down.png")
playerLeft = pygame.image.load("./image/player/move_left.png")
playerRight = pygame.image.load("./image/player/move_right.png")

TIME = 5


class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.surface = pygame.Surface((100, 100), pygame.SRCALPHA)
        self.surface.blit(playerDown, (20, 20), (0, 0, 60, 60))
        self.timeSkip = 0
        self.option = 0

        self.go = 0

    def update(self, up, down, left, right):

        if self.go < 100:
            if self.timeSkip <= TIME:  # 0 - 5
                self.option = 0
            elif self.timeSkip <= TIME*2:  # 6 - 10
                self.option = 1
            elif self.timeSkip <= TIME*3:  # 11 - 15
                self.option = 2
            elif self.timeSkip <= TIME*4:
                self.option = 3
            elif self.timeSkip <= TIME*5:
                self.option = 4

            elif self.timeSkip > TIME*5:
                self.timeSkip = 0

            if up or down or left or right:
                self.surface.fill((0, 0, 0, 0))
                self.timeSkip += 1
                self.animate(up, down, left, right)
                self.go += 2

            if up:
                self.y -= 2

            elif down:
                self.y += 2

            elif left:
                self.x -= 2

            elif right:
                self.x += 2
        else:
            self.go = 0

    def animate(self, up, down, left, right):
        img = ""
        if up:
            img = playerUp
        elif down:
            img = playerDown
        elif left:
            img = playerLeft
        elif right:
            img = playerRight

        if self.option == 0:
            self.surface.blit(img, (20, 20), (0, 0, 60, 60))
        if self.option == 1:
            self.surface.blit(img, (20, 20), (60, 0, 60, 60))
        if self.option == 2:
            self.surface.blit(img, (20, 20), (120, 0, 60, 60))
        if self.option == 3:
            self.surface.blit(img, (20, 20), (180, 0, 60, 60))
        if self.option == 4:
            self.surface.blit(img, (20, 20), (240, 0, 60, 60))

    def draw(self):
        DISPLAYSURF.blit(self.surface, (self.x, self.y))


def main():
    player = Player()
    up, down, left, right = False, False, False, False
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            if event.type == KEYDOWN:
                if event.key == K_UP:
                    up = True
                if event.key == K_DOWN:
                    down = True
                if event.key == K_LEFT:
                    left = True
                if event.key == K_RIGHT:
                    right = True


        DISPLAYSURF.blit(surfaceMap, (0, 0))
        player.draw()
        player.update(up, down, left, right)

        if player.go == 0:
            up, down, left, right = False, False, False, False

        pygame.display.update()
        pygame.time.Clock().tick(60)


main()
