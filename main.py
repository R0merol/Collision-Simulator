"""
Main Program File
"""

import pygame
import sys

# Initialize pygame
pygame.init()
clock = pygame.time.Clock()
TARGET_FPS = 60
FPS = 60

# Initiate screen
screen_width = 800
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

# Set caption, icon
pygame.display.set_caption("Collision Simulator!")

# Terminal colors
L_GREEN = pygame.Color("#5ec830")
GREEN = pygame.Color("#1c4811")
D_GREEN = pygame.Color("#255517")
XD_GREEN = pygame.Color("#071404")
RED = pygame.Color("#f41919")
BLUE = pygame.Color("#32f4f4")
WHITE = pygame.Color("#ffffff")


class Program:
    def __init__(self):
        self.moving_rect = pygame.Rect(350, 350, 100, 100)
        self.x_speed, self.y_speed = 5, 5

        self.other_rect = pygame.Rect(300, 100, 200, 100)
        self.other_speed = 2

    def run(self, dt):
        self.bouncing_rect(dt)

    def bouncing_rect(self, dt):
        self.moving_rect.x += self.x_speed * dt
        self.moving_rect.y += self.y_speed * dt

        # Collision with screen borders
        if self.moving_rect.right >= screen_width or self.moving_rect.left <= 0:
            self.x_speed *= -1
        if self.moving_rect.bottom >= screen_height or self.moving_rect.top <= 0:
            self.y_speed *= -1

        # Moving the other rectangle
        self.other_rect.y += self.other_speed
        if self.other_rect.top <= 0 or self.other_rect.bottom >= screen_height:
            self.other_speed *= -1

        # Collision with rect
        collision_tolerance = 10
        if self.moving_rect.colliderect(self.other_rect):
            if abs(self.other_rect.top - self.moving_rect.bottom) < collision_tolerance and self.y_speed > 0:
                self.y_speed *= -1
            if abs(self.other_rect.bottom - self.moving_rect.top) < collision_tolerance and self.y_speed < 0:
                self.y_speed *= -1
            if abs(self.other_rect.right - self.moving_rect.left) < collision_tolerance and self.x_speed < 0:
                self.x_speed *= -1
            if abs(self.other_rect.left - self.moving_rect.right) < collision_tolerance and self.x_speed > 0:
                self.x_speed *= -1

        pygame.draw.rect(screen, BLUE, self.moving_rect)
        pygame.draw.rect(screen, L_GREEN, self.other_rect)


def main():
    # Initiate instances
    program = Program()

    while True:
        # Calculate delta time
        dt = clock.tick(FPS) * .001 * TARGET_FPS

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Run game
        program.run(dt)

        # Updates
        pygame.display.flip()
        screen.fill(XD_GREEN)


if __name__ == '__main__':
    main()
