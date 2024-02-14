"""Файл для работы с pygame"""


from random import choice
from objects import *


class Game:
    """Класс для работы с pygame."""
    def __init__(self, screen_width: int = 480,
                 screen_height: int = 720, w: int = 10, h: int = 15) -> None:
        """Инициализация объекта игры."""
        pg.init()

        self.__tile: int = 48
        self.__size: tuple = (w, h)

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

        self.__grid: list = [pg.Rect(x * self.__tile,
                                     y * self.__tile,
                                     self.__tile,
                                     self.__tile)
                             for x in range(self.__size[0])
                             for y in range(self.__size[1])
                             ]
        # Создание фигуры
        self.__figure = FigureZ(self.__size[0])

    def __del__(self) -> None:
        """Очистка памяти по итогу работы."""
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
        """Проверка событий в игровом цикле."""
        event: pg.event.Event
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.__game_run = False

    def __move(self) -> None:
        """Движение игрока."""
        pass

    def __check_logic(self) -> None:
        """Игровая логика."""
        pass

    def __draw(self) -> None:
        """Рисование всех объектов."""

        self.__screen.fill(self.__color_bg)
        [pg.draw.rect(self.__screen, (40, 40, 40), i_rect, 1) for i_rect in self.__grid]

        self.__figure.draw_figure(self.__screen, self.__tile)

        pg.display.flip()
        self.__clock.tick(self.__fps)
