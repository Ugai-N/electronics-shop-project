import csv

FILE_PATH = 'D:\\Study\\DZ\\electronics-shop-project\\src\\items.csv'


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) <= 10:
            self.__name = name
        elif isinstance(name, str) and len(name) > 10:
            self.__name = name[:10]
        else:
            raise ValueError('Некорректное название')

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        Item.all.clear()
        with open(FILE_PATH, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = row["name"]
                price = float(row['price'])
                quantity = int(row['quantity'])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(string):
        if string.isdigit():
            return int(string)
        else:
            try:
                float(string)
                return int(float(string))
            except ValueError:
                raise ValueError
