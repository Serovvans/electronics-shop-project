import pytest

from src.item import Item
from src.phone import Phone
from src.keyboard import Keyboard


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


@pytest.fixture(scope="session")
def keyboard() -> Keyboard:
    """Фикстура Keyboard класса Keyboard"""
    return Keyboard('Dark Project KD87A', 9600, 5)
