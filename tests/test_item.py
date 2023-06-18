"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)
item3 = Item("Кабель", 10, 5)


def test_item():
    assert item1.name == 'Смартфон'
    assert item1.price == 10000
    assert item1.quantity == 20


def test_calculate_total_price():
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_apply_discount():
    Item.pay_rate = 0.8
    item3.pay_rate = 0.5
    item1.apply_discount()
    item3.apply_discount()
    assert item1.price == 8000.0
    assert item2.price == 20000
    assert item3.price == 5


def test_list_items():
    assert Item.all == [item1, item2, item3]
