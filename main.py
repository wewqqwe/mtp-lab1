"""Точка входа: краткая сводка по текстовому файлу.

Запуск:
    python main.py [путь к файлу]

Без аргумента используется образец из папки ``data``.
"""

import sys

from text_loader import TextNotFoundError, describe, load_text

#: файл, который берётся, когда путь не указан явно
DEFAULT_PATH = "data/sample.txt"


def main(argv):
    """Показать сводку по тексту.

    :param argv: аргументы командной строки без имени программы
    :return: код возврата процесса
    """
    path = argv[0] if argv else DEFAULT_PATH

    try:
        text = load_text(path)
    except TextNotFoundError as error:
        print(error)
        return 1

    summary = describe(text)
    print("Файл: %s" % path)
    print("Символов: %d" % summary["symbols"])
    print("Строк: %d" % summary["lines"])
    print("Непустых строк: %d" % summary["filled_lines"])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
