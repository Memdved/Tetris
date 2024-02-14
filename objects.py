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

    def __init__(self):
        super().__init__()

        self.__blocks: list = [self.sprite.get_rect() for _ in range(4)]
