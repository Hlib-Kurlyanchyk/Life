import time
import pygame
import random
from pygame.locals import *


class GameOfLife:

    def __init__(self, width: int = 640, height: int = 480, cell_size: int = 10, speed: int = 0.1) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed

    def draw_lines(self) -> None:
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), (0, y), (self.width, y))

    def run(self) -> None:
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        grid = game.create_grid(True)
        self.draw_grid(grid)
        self.draw_lines()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

            self.screen.fill(pygame.Color('white'))
            grid = self.get_next_generation(grid)
            self.draw_grid(grid)
            self.draw_lines()
            time.sleep(self.speed)
            pygame.display.flip()
        pygame.quit()

    def create_grid(self, randomize: bool = False):
        if randomize is True:
            grid = [[random.randint(0, 1) for k in range(self.cell_height)] for i in range(self.cell_width)]
        else:
            grid = [[0 for k in range(self.cell_height)] for i in range(self.cell_width)]
        return grid

    def draw_grid(self, grid: list) -> None:
        for i in range(self.cell_width):
            for k in range(self.cell_height):
                if grid[i][k] == 1:
                    pygame.draw.rect(self.screen, pygame.Color('green'), (i*20, k*20, self.cell_size, self.cell_size))

    def neighbours(self, grid: list, pos: list, system=None):
        if system is None:
            system = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        count = 0
        for i in system:
            if grid[(pos[0] + i[0]) % len(grid)][(pos[1] + i[1]) % len(grid[0])]:
                count += 1
        return count

    def get_next_generation(self, grid: list):
        new_grid = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # Если клетка жива
                if grid[i][j]:
                    # Если у соседей не 2 или 3 соседа
                    if self.neighbours(grid, [i, j]) not in (2, 3):
                        new_grid[i][j] = 0
                        continue
                    # В ином случае
                    new_grid[i][j] = 1
                    continue
                # Если клетка мертва и у неё 3 соседа
                if self.neighbours(grid, [i, j]) == 3:
                    new_grid[i][j] = 1
                    continue
                # В противном случае
                new_grid[i][j] = 0
        return new_grid


if __name__ == '__main__':
    game = GameOfLife(640, 480, 20)
    game.run()
