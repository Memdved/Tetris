"""Файл для создания объектов(фигур)"""


import pygame as pg
from random import randint


class Figures:
    """Родительский класс фигур для создания фигур."""
    image_width: int = 48
    image_height: int = 48

    def __init__(self, color: int = randint(0, 4)) -> None:
        """Инициализация фигуры"""
        self.sprite = pg.transform.scale(
            pg.image.load(f"sprites/block{color}.png").convert(),
            (self.image_width, self.image_height)
        )


class FigureO(Figures):
    __pos: list[
        tuple[int, int],
        tuple[int, int],
        tuple[int, int],
        tuple[int, int]
    ] = [(0, 0), (-1, -1), (0, -1), (-1, 0)]

    def __init__(self, w):
        super().__init__()

        self.__figure = [pg.Rect(x + w // 2, y + 1, 1, 1) for x, y in self.__pos]
        self.__figure_rect = self.sprite.get_rect()

    def draw_figure(self, sc: pg.Surface, tile):
        for _ in range(4):
            self.__figure_rect.x = self.__figure[_].x * tile
            self.__figure_rect.y = self.__figure[_].y * tile
            sc.blit(self.sprite, (self.__figure_rect.x, self.__figure_rect.y))


class FigureI(Figures):
    __pos: list[
        tuple[int, int],
        tuple[int, int],
        tuple[int, int],
        tuple[int, int]
    ] = [(-1, -1), (-2, -1), (0, -1), (1, -1)]

    def __init__(self, w):
        super().__init__()

        self.__figure = [pg.Rect(x + w // 2, y + 1, 1, 1) for x, y in self.__pos]
        self.__figure_rect = self.sprite.get_rect()

    def draw_figure(self, sc: pg.Surface, tile):
        for _ in range(4):
            self.__figure_rect.x = self.__figure[_].x * tile
            self.__figure_rect.y = self.__figure[_].y * tile
            sc.blit(self.sprite, (self.__figure_rect.x, self.__figure_rect.y))


class FigureS(Figures):
    __pos: list[
        tuple[int, int],
        tuple[int, int],
        tuple[int, int],
        tuple[int, int]
    ] = [(0, 0), (-1, -1), (-1, 0), (0, 1)]

    def __init__(self, w):
        super().__init__()

        self.__figure = [pg.Rect(x + w // 2, y + 1, 1, 1) for x, y in self.__pos]
        self.__figure_rect = self.sprite.get_rect()

    def draw_figure(self, sc: pg.Surface, tile):
        for _ in range(4):
            self.__figure_rect.x = self.__figure[_].x * tile
            self.__figure_rect.y = self.__figure[_].y * tile
            sc.blit(self.sprite, (self.__figure_rect.x, self.__figure_rect.y))

