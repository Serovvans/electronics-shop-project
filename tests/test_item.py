"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_total_price(item_smartphone, item_laptop):
    """Тест получения стоимости всех товаров одного вида в наличии"""
    assert item_smartphone.calculate_total_price() == 200000, "Неверно высчитана стоимость всех товаров в наличии"
    assert item_laptop.calculate_total_price() == 100000, "Неверно высчитана стоимость всех товаров в наличии"


def test_apply_discount(item_smartphone, item_laptop):
    """Тестирует изменение и применение скидки на товар"""
    last = item_smartphone.price
    last1 = item_laptop.price
    Item.pay_rate = 0.8
    item_smartphone.apply_discount()

    assert item_smartphone.price == 8000.0, "Неверно применена скидка"
    assert item_laptop.price == 20000, "Неверно применена скидка"

    item_smartphone.price = last
    item_laptop = last1


def test_list_of_items(item_smartphone, item_laptop):
    """Тестирует добавление экземпляров в атрибут класса"""
    assert len(Item.all) == 2


def test_name(item_smartphone):
    """Тестирует геттер и сеттер атрибута name"""
    assert item_smartphone.name == "Смартфон"
    item_smartphone.name = "SuperСмартфон"
    assert item_smartphone.name == "SuperСмарт"
    item_smartphone.name = "Смартфон"


def test_instantiate_from_csv():
    """Тестирует чтение данных из csv файла"""
    Item.instantiate_from_csv()  # создание объектов из данных файла
    assert len(Item.all) == 5

    item1 = Item.all[0]
    assert item1.name == 'Смартфон'


def test_string_to_number():
    """Тестирует классовый метод перевода"""
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr(item_smartphone):
    """Тестирует представление объекта для отладчика"""
    assert repr(item_smartphone) == "Item('Смартфон', 10000, 20)"


def test_str(item_smartphone):
    """Тестирует строковое представление объекта"""
    assert str(item_smartphone) == 'Смартфон'


def test_add(item_smartphone, item_laptop):
    assert item_smartphone + item_laptop == 25
