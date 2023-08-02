"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_total_price(item_smartphone ,item_laptop):
    """Тест получения стоимости всех товаров одного вида в наличии"""
    assert item_smartphone.calculate_total_price() == 200000, "Неверно высчитана стоимость всех товаров в наличии"
    assert item_laptop.calculate_total_price() == 100000, "Неверно высчитана стоимость всех товаров в наличии"


def test_apply_discount(item_smartphone, item_laptop):
    """Тестирует изменение и применение скидки на товар"""
    Item.pay_rate = 0.8
    item_smartphone.apply_discount()

    assert item_smartphone.price == 8000.0, "Неверно применена скидка"
    assert item_laptop.price == 20000, "Неверно применена скидка"


def test_list_of_items(item_smartphone, item_laptop):
    """Тестирует добавление экземпляров в атрибут класса"""
    assert len(Item.all) == 2
