import pytest

from main import generator_of_greeting_message


@pytest.mark.parametrize(
    'name,expected', [
        ('Никита', 'Привет, Никита'),
        ('Ольга', 'Привет, Ольга'),
    ],
)
def test_greeting(name: str, expected: str):
    """Текст приветствия зависит от имени."""
    assert generator_of_greeting_message(name) == expected


def test_capitalize():
    """Все слова в имени начинаются с большой буквы."""
    name = 'яндекс практикум'
    assert generator_of_greeting_message(name) == 'Привет, Яндекс Практикум'
