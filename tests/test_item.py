"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture
def item1():
    item1 = Item("Смартфон", 10000, 20)
    return item1


@pytest.fixture
def item2():
    item2 = Item("Ноутбук", 20000, 5)
    return item2


@pytest.fixture
def item3():
    item3 = Item("Кабель", 10, 5)
    return item3


@pytest.fixture
def item():
    item = Item('Телефон', 10000, 5)
    return item


def test_init_item(item1):
    assert item1.name == 'Смартфон'
    assert item1.price == 10000
    assert item1.quantity == 20


def test_repr_item(item3):
    assert repr(item3) == "Item('Кабель', 10, 5)"


def test_str_item(item3):
    assert str(item3) == 'Кабель'


def test_property_setter_name(item):
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'
    item.name = "СуперСмартфон"
    assert item.name == "СуперСмарт"
    item.name = '123'
    assert item.name == '123'
    with pytest.raises(ValueError):
        item.name = 123


def test_calculate_total_price(item1, item2):
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_apply_discount(item1, item2, item3):
    Item.pay_rate = 0.8
    item3.pay_rate = 0.5
    item1.apply_discount()
    item3.apply_discount()
    assert item1.price == 8000.0
    assert item2.price == 20000
    assert item3.price == 5


def test_instantiate_from_csv(item3):
    Item.instantiate_from_csv()
    assert Item.all[3].name == 'Мышка'
    assert Item.all[3].price == 50
    assert Item.all[3].quantity == 5
    assert len(Item.all) == 5
    assert Item.all[0].name == 'Смартфон'


def test_string_to_number():
    assert Item.string_to_number('123') == 123
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
    with pytest.raises(ValueError):
        Item.string_to_number('abc123')
