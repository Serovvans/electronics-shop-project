import os

from csv import DictReader
from src.exceptions import InstantiateCSVError


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

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.quantity * self.price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self) -> str:
        """Геттер для атрибута name"""
        return self.__name

    @name.setter
    def name(self, new_value: str):
        """Сеттер для атрибута name"""
        if len(new_value) > 10:
            new_value = new_value[:10]
        self.__name = new_value

    @classmethod
    def instantiate_from_csv(cls):
        """
        Создание экземпляра класса из файла с данными
        """
        file: str = os.path.join("..", "src", "items.csv")
        cls.all = []
        try:
            with open(file, "r") as f:
                data = DictReader(f)

                for item in data:
                    cls(item["name"], item["price"], item["quantity"])
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл items.csv")
        except KeyError:
            raise InstantiateCSVError("Файл item.csv поврежден")

    @staticmethod
    def string_to_number(value: str) -> int:
        """
        Перевод из строки в число типа int
        """
        try:
            return int(float(value))
        except ValueError:
            print("Некорректное значение")

    def __repr__(self):
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        raise ValueError("Оба объекта должны быть подклассом Item")
