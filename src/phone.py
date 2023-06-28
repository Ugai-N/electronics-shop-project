from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """
        Создание экземпляра класса phone (дочернего item).
        :param number_of_sim: кол-во поддерживаемых сим-карт.
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        """Переопределение repr Item, возвращает инфо в формате 'Item(<name>, <price>, <quantity>, <number_of_sim>)'"""
        return f"{self.__class__.__name__}({self.name!r}, {self.price}, {self.quantity}, {self.__number_of_sim})"

    @property
    def number_of_sim(self):
        """Геттер для вызова приватного атрибута <number_of_sim>"""
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        """
        Setter для <number_of_sim>: проверяет, что значение - целое число больше нуля.
        Если нет - ValueError
        """
        if (isinstance(number_of_sim, int) or number_of_sim.isdigit()) and int(number_of_sim) > 0:
            self.__number_of_sim = int(number_of_sim)
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')
