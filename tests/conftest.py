import pytest

from src.item import Item
from src.phone import Phone


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


@pytest.fixture
def alien1():
    class Alien:
        def __init__(self, name: str, price: float, quantity: int) -> None:
            self.__name = name
            self.price = price
            self.quantity = quantity

    alien1 = Alien("alien1", 10_000, 5)
    return alien1


@pytest.fixture
def phone1():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    return phone1
