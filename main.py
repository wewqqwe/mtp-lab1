"""Точка входа: сводка и частотный список слов текстового файла.

Запуск:
    python main.py [путь к файлу] [сколько слов показать]

Без аргументов берётся образец из папки ``data`` и пять самых
частых слов.
"""

import sys

from frequency import most_common, unique_ratio
from text_loader import TextNotFoundError, describe, load_text

#: файл, который берётся, когда путь не указан явно
DEFAULT_PATH = "data/sample.txt"

#: сколько слов показывать, когда число не указано
DEFAULT_LIMIT = 5


def read_limit(argv):
    """Определить, сколько слов показывать.

    :param argv: аргументы командной строки без имени программы
    :return: положительное число слов
    """
    if len(argv) < 2:
        return DEFAULT_LIMIT

    try:
        limit = int(argv[1])
    except ValueError:
        print("Второй аргумент должен быть числом, беру %d" % DEFAULT_LIMIT)
        return DEFAULT_LIMIT

    return limit if limit > 0 else DEFAULT_LIMIT


def main(argv):
    """Показать сводку и частотный список слов.

    :param argv: аргументы командной строки без имени программы
    :return: код возврата процесса
    """
    path = argv[0] if argv else DEFAULT_PATH
    limit = read_limit(argv)

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
    print("Доля уникальных слов: %s" % unique_ratio(text))

    print("Самые частые слова:")
    for word, count in most_common(text, limit):
        print("  %-14s %d" % (word, count))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
