from src.item import Item


class MixinChange:
    """Класс добавления функционала смены языка"""
    def __init__(self, name: str, price: float, quantity: int, language: str):
        """Инициализация данных через класс Item и добавление аттрибута языка"""
        super().__init__(name, price, quantity)
        self.__language = language

    @property
    def language(self):
        """Getter для языка раскладки"""
        return self.__language

    def change_lang(self):
        """Метод смены языка раскладки"""
        if self.__language == "RU":
            self.__language = "EN"
        elif self.__language == "EN":
            self.__language = "RU"
        else:
            raise AttributeError("Неверная раскладка клавиатуры. Ожидается RU/EN")
        return self


class Keyboard(MixinChange, Item):
    """Класс представления для товара клавиатуры"""
    def __init__(self,  name: str, price: float, quantity: int, language: str = "EN"):
        """Инициализация объекта клавиатуры через класс MixinChange"""
        super().__init__(name, price, quantity, language)
