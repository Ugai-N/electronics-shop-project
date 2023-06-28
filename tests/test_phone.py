import pytest

from src.item import Item
from src.phone import Phone


def test_init_phone(phone1):
    assert phone1.name == 'iPhone 14'
    assert phone1.price == 120_000
    assert phone1.quantity == 5
    assert phone1.number_of_sim == 2
    assert len(phone1.__dict__) == 4


def test_subclass_phone(phone1):
    assert isinstance(phone1, Item)
    assert issubclass(Phone, Item)


def test_repr_phone(phone1):
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_str_phone(phone1):
    assert str(phone1) == 'iPhone 14'


def test_add_phone(item1, phone1, alien1):
    assert phone1 + phone1 == 10
    assert phone1 + item1 == 25
    with pytest.raises(ValueError):
        phone1 + 10
    with pytest.raises(ValueError):
        phone1 + alien1


def test_number_of_sim(phone1):
    phone1.number_of_sim = 4
    assert phone1.number_of_sim == 4
    phone1.number_of_sim = '1'
    assert phone1.number_of_sim == 1
    with pytest.raises(ValueError, match='Количество физических SIM-карт должно быть целым числом больше нуля'):
        phone1.number_of_sim = 0
    with pytest.raises(ValueError, match='Количество физических SIM-карт должно быть целым числом больше нуля'):
        phone1.number_of_sim = 'две'
