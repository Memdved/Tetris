"""Файл для создания объектов(фигур)"""

import pygame as pg
from random import randint
from copy import deepcopy


class Figures:
    """Класс фигур для создания фигур."""
    image_width: int = 48
    image_height: int = 48

    __pos = {0: [(0, 0), (-1, -1), (0, -1), (-1, 0)],
             1: [(-1, -1), (-2, -1), (0, -1), (1, -1)],
             2: [(0, 0), (-1, -1), (-1, 0), (0, 1)],
             3: [(-1, 0), (0, 0), (-1, 1), (0, -1)],
             4: [(0, 0), (-1, 0), (0, -1), (0, 1)],
             5: [(0, 0), (-1, -1), (0, -1), (0, 1)],
             6: [(0, 0), (1, -1), (0, -1), (0, 1)],
             }

    def __init__(self, w: int, h: int, color: int = randint(0, 4)) -> None:
        """Инициализация фигуры"""
        self.sprite = pg.transform.scale(
            pg.image.load(f"sprites/block{color}.png").convert(),
            (self.image_width, self.image_height)
        )

        self.__w = w
        self.__h = h

        self.__figure = deepcopy([pg.Rect(x + self.__w // 2, y + 1, 1, 1) for x, y in self.__pos[randint(0, 6)]])
        self.figure_rect = self.sprite.get_rect()

        self.dx = 0

        self.__frame_count = 0
        self.frame_limit = 5
        self.__dy = 1

    def __check_borders_x(self, i):
        if self.__figure[i].x < 0 or self.__figure[i].x > self.__w - 1:
            return False
        return True

    def __check_borders_y(self, j, field):
        if self.__figure[j].y < self.__h - 1 and field[self.__figure[j].y + 1][self.__figure[j].x] == 0:
            return False
        return True

    def move_figure(self, field):
        figure_old = deepcopy(self.__figure)
        self.__frame_count += 1
        for i in range(4):
            if self.__check_borders_y(i, field):
                new_field = self.__change_figure(field)
                self.__frame_count = 0
                return new_field

            elif self.__frame_count % self.frame_limit == 1:
                self.__figure[i].y += self.__dy

            self.__figure[i].x += self.dx
            if not self.__check_borders_x(i):
                self.__figure = deepcopy(figure_old)
                break

        self.__frame_count += 1
        self.dx = 0
        return field

    def __change_figure(self, field):
        color: int = randint(0, 4)

        field[self.__figure[0].y][self.__figure[0].x] = self.sprite
        field[self.__figure[1].y][self.__figure[1].x] = self.sprite
        field[self.__figure[2].y][self.__figure[2].x] = self.sprite
        field[self.__figure[3].y][self.__figure[3].x] = self.sprite

        self.sprite = pg.transform.scale(
            pg.image.load(f"sprites/block{color}.png").convert(),
            (self.image_width, self.image_height)
        )

        self.__figure = deepcopy([pg.Rect(x + self.__w // 2, y + 1, 1, 1) for x, y in self.__pos[randint(0, 6)]])
        self.figure_rect = self.sprite.get_rect()

        return field

    def draw_figure(self, sc: pg.Surface, tile):
        for _ in range(4):
            self.figure_rect.x = self.__figure[_].x * tile
            self.figure_rect.y = self.__figure[_].y * tile
            sc.blit(self.sprite, (self.figure_rect.x, self.figure_rect.y))
