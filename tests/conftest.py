import pytest

from src.item import Item


@pytest.fixture(scope="module")
def item_smartphone() -> Item:
    """Фикстура объекта товара Смартфон"""
    return Item("Смартфон", 10000, 20)


@pytest.fixture(scope="module")
def item_laptop() -> Item:
    """Фикстура объекта товара Ноутбук"""
    return Item("Ноутбук", 20000, 5)
