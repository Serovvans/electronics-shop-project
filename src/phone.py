from src.item import Item


class Phone(Item):
    """
    Класс для представления товара типа телефон. Наследуется от класса товар
    """
    def __init__(self, name: str, price: float, quantity: int, number_of_sim):
        """
        Создание экземпляра класса Phone.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :number_of_sim: Количество доступных сим-карт
        """
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
