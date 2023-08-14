import pytest

from src.item import Item
from src.phone import Phone


@pytest.fixture(scope="module")
def item_smartphone() -> Item:
    """Фикстура объекта товара Смартфон"""
    return Item("Смартфон", 10000, 20)


@pytest.fixture(scope="module")
def item_laptop() -> Item:
    """Фикстура объекта товара Ноутбук"""
    return Item("Ноутбук", 20000, 5)


@pytest.fixture(scope="module")
def phone1() -> Phone:
    """Фикстура iPhone класса Phone"""
    return Phone("iPhone 14", 120_000, 5, 2)
