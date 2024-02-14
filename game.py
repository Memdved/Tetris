"""Файл для работы с pygame"""


import pygame as pg


class Game:
    def __init__(self, screen_width: int = 480,
                 screen_height: int = 720) -> None:
        """Инициализация объекта игры."""
        pg.init()

        self.__screen_width: int = screen_width
        self.__screen_height: int = screen_height
        self.__screen: pg.Surface = \
            pg.display.set_mode(
                (self.__screen_width,
                 self.__screen_height)
            )

        self.__color_bg: tuple[int, int, int] = (0, 0, 0)  # Черный цвет

        self.__fps: int = 60
        self.__clock: pg.time.Clock = pg.time.Clock()
        self.__game_run: bool = True

    def __del__(self) -> None:
        """Очистка памяти по итогу работы"""
        pg.quit()

    def run(self) -> None:
        """Запуск игрового цикла игры."""

        while self.__game_run:
            self.__check_events()
            self.__move()
            self.__check_logic()
            self.__draw()

            self.__clock.tick(self.__fps)

    def __check_events(self) -> None:
        """Проверка событий в игровом цикле"""
        event: pg.event.Event
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.__game_run = False

    def __move(self) -> None:
        """Движение игрока"""
        pass

    def __check_logic(self) -> None:
        """Игровая логика"""
        pass

    def __draw(self) -> None:
        """Рисование всех объектов"""

        self.__screen.fill(self.__color_bg)

        pg.display.flip()
        self.__clock.tick(self.__fps)
