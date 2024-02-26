"""Файл для работы с pygame"""


from objects import Figures
import pygame as pg
import pandas as pd


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

        self.__fps: int = 30
        self.__clock: pg.time.Clock = pg.time.Clock()
        self.__game_run: bool = True

        self.__grid: list = [pg.Rect(x * self.__tile,
                                     y * self.__tile,
                                     self.__tile,
                                     self.__tile)
                             for x in range(self.__size[0])
                             for y in range(self.__size[1])
                             ]

        self.field = [[0 for i in range(w)] for j in range(h)]

        # Создание фигуры
        self.__figure = Figures(w, h)

        df = pd.DataFrame(self.field)
        print(df)

    def __del__(self) -> None:
        """Очистка памяти по итогу работы."""
        pg.quit()

    def run(self) -> None:
        """Запуск игрового цикла игры."""

        while self.__game_run:
            self.__check_events()
            self.__move()
            self.__draw()

            self.__clock.tick(self.__fps)

    def __check_events(self) -> None:
        """Проверка событий в игровом цикле."""
        event: pg.event.Event
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.__game_run = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    self.__figure.dx = -1
                elif event.key == pg.K_RIGHT:
                    self.__figure.dx = 1
                elif event.key == pg.K_DOWN:
                    self.__figure.frame_limit = 2
            elif event.type == pg.KEYUP:
                if event.key == pg.K_DOWN:
                    self.__figure.frame_limit = 30

    def __move(self) -> None:
        """Движение игрока."""
        self.field = self.__figure.move_figure(self.field)

    def __draw(self) -> None:
        """Рисование всех объектов."""

        self.__screen.fill(self.__color_bg)
        [pg.draw.rect(self.__screen, (40, 40, 40), i_rect, 1) for i_rect in self.__grid]

        self.__figure.draw_figure(self.__screen, self.__tile)

        for y, raw in enumerate(self.field):
            for x, col in enumerate(raw):
                if col != 0:
                    self.__figure.figure_rect.x, self.__figure.figure_rect.y = x * self.__tile, y * self.__tile
                    self.__screen.blit(col, (self.__figure.figure_rect.x, self.__figure.figure_rect.y))

        pg.display.flip()
        self.__clock.tick(self.__fps)
