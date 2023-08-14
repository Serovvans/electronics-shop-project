def test_sim_count(phone1):
    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone1.number_of_sim == 2


def test_add(phone1, item_smartphone):
    item1 = item_smartphone

    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
