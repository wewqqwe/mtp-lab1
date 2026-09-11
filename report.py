"""Отчёт по частотам слов в виде текстовой таблицы.

Модуль отделён от ``main``: сбор данных и их оформление — разные
задачи, и менять вид таблицы можно, не трогая разбор аргументов.
"""

from frequency import count_words, most_common

#: ширина столбца со словом
WORD_COLUMN = 16

#: ширина полосы, изображающей частоту
BAR_WIDTH = 24


def build_bar(count, top_count, width=BAR_WIDTH):
    """Построить полосу, пропорциональную частоте слова.

    :param count: частота слова
    :param top_count: наибольшая частота в выборке
    :param width: длина полосы для наибольшей частоты
    :return: строка из символов ``#``
    """
    if top_count <= 0:
        return ""
    length = max(1, round(count / top_count * width))
    return "#" * length


def build_table(text, limit=5):
    """Собрать таблицу самых частых слов.

    :param text: исходный текст
    :param limit: сколько строк в таблице
    :return: список строк отчёта
    """
    rows = most_common(text, limit)
    if not rows:
        return ["Значимых слов в тексте нет."]

    top_count = rows[0][1]
    total = sum(count_words(text).values())

    lines = ["%-*s %6s %7s  %s" % (WORD_COLUMN, "Слово", "Раз", "Доля", "")]
    lines.append("-" * (WORD_COLUMN + BAR_WIDTH + 16))
    for word, count in rows:
        share = count / total * 100 if total else 0.0
        lines.append("%-*s %6d %6.1f%%  %s" % (
            WORD_COLUMN, word, count, share, build_bar(count, top_count)))
    return lines


def render(text, limit=5):
    """Оформить таблицу одной строкой с переносами.

    :param text: исходный текст
    :param limit: сколько строк в таблице
    :return: готовый текст отчёта
    """
    return "\n".join(build_table(text, limit))
