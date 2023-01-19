"""Генератор приветствий."""


def set_first_letters_to_uppercase(source_value: str) -> str:
    """Возвращает строку.

    Возвращает строку с первыми заглавнными
    буквами в отдельных словах.

    Args:
        source_value: Исходная строка

    Returns:
        str: строка с первыми заглавными буквами
    """
    source_value = source_value.split(' ')
    for index, word in enumerate(source_value):
        first_upper_letter = source_value[index][0].upper()
        source_value[index] = first_upper_letter + word[1:]
    return ' '.join(source_value)


def generator_of_greeting_message(name: str) -> str:
    """
    Возвращает текст приветствия с заглавными буквами в начале слов имени.

    Args:
        name: Имя пользователя

    Returns:
        str: Текст приветствия
    """
    formatted_name = set_first_letters_to_uppercase(name)
    return 'Привет, {0}'.format(formatted_name)
