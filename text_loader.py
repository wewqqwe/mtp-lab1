"""Загрузка текста из файла.

Модуль отвечает только за чтение: он не разбирает текст на слова
и не считает статистику. Такое разделение позволяет подменить
источник данных, не трогая остальной код.
"""

import io
import os


class TextNotFoundError(FileNotFoundError):
    """Запрошенный текстовый файл отсутствует."""


def load_text(path):
    """Прочитать текст из файла в кодировке UTF-8.

    :param path: путь к текстовому файлу
    :return: содержимое файла одной строкой
    :raises TextNotFoundError: если файла нет на диске
    """
    if not os.path.isfile(path):
        raise TextNotFoundError("Файл не найден: %s" % path)

    with io.open(path, "r", encoding="utf-8") as source:
        return source.read()


def describe(text):
    """Собрать краткую сводку по тексту.

    :param text: исходный текст
    :return: словарь с числом символов, строк и непустых строк
    """
    lines = text.splitlines()
    return {
        "symbols": len(text),
        "lines": len(lines),
        "filled_lines": sum(1 for line in lines if line.strip()),
    }
