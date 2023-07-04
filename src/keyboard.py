from src.item import Item


class MixinLang:
    def __init__(self, name, price, quantity):
        """Миксин для экземпляров класса Keyboard с функциональностью по изменению раскладки клавиатуры
        Язык по умолчанию EN. Всего поддерживается два языка: EN и RU.
        Изменить язык можно только методом change_lang()"""
        super().__init__(name, price, quantity)  # передаем аргументы в след.родителя
        self.__language = 'EN'

    @property
    def language(self):
        """Геттер для вызова приватного атрибута <language>"""
        return self.__language

    def change_lang(self):
        """Меняет раскладку клавиатуры на второй язык. Возвращает self"""
        if self.__language == 'EN':
            self.__language = 'RU'
        elif self.__language == 'RU':
            self.__language = 'EN'
        return self


class Keyboard(MixinLang, Item):
    def __init__(self, name: str, price: float, quantity: int) -> None:
        """Создание экземпляра класса Keyboard (дочернего Item и MixinLang).
        Первым вызываем инициализатор MixinLang, чтобы не корректировать Item,
        прокидывая аргументы для инициализации Item"""
        super().__init__(name, price, quantity)  # передаем аргументы в перв. слева родителя
