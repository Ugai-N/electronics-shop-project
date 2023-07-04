import pytest

from src.item import Item
from src.keyboard import MixinLang, Keyboard


def test_init_keyboard(kb1):
    assert kb1.name == 'Dark Project KD87A'
    assert kb1.price == 9600
    assert kb1.quantity == 5
    assert kb1.language == 'EN'
    assert isinstance(kb1, (Item, MixinLang))
    assert ', '.join(cl.__name__ for cl in Keyboard.__mro__[0:3]) == 'Keyboard, MixinLang, Item'


def test_lang_property(kb1):
    with pytest.raises(AttributeError, match="property 'language' of 'Keyboard' object has no setter"):
        kb1.language = 'RU'


def test_change_lang(kb1):
    assert kb1.language == 'EN'
    kb1.change_lang()
    assert kb1.language == 'RU'
    kb1.change_lang().change_lang()
    assert kb1.language == 'RU'
