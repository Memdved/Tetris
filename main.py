"""Основной исполняемый файл"""


from game import Game


def main() -> None:
    """Исполняемая функция"""

    game = Game()
    game.run()


if __name__ == "__main__":
    main()
