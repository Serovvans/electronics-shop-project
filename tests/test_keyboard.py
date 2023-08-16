def test_attrs(keyboard):
    assert str(keyboard) == "Dark Project KD87A"
    assert str(keyboard.language) == "EN"


def test_change_lang(keyboard):
    keyboard.change_lang()
    assert str(keyboard.language) == "RU"

    # Сделали RU -> EN -> RU
    keyboard.change_lang().change_lang()
    assert str(keyboard.language) == "RU"
