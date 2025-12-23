from string_utils import StringUtils


def test_capitalize_positive():
    utils = StringUtils()
    result = utils.capitalize("skypro")
    assert result == "Skypro"


def test_capitalize_empty_string():
    utils = StringUtils()
    result = utils.capitalize("")
    assert result == ""


def test_trim_positive():
    utils = StringUtils()
    result = utils.trim("   skypro")
    assert result == "skypro"


def test_trim_empty_string():
    utils = StringUtils()
    result = utils.trim("")
    assert result == ""


def test_contains_positive():
    utils = StringUtils()
    result = utils.contains("SkyPro", "S")
    assert result is True


def test_contains_negative():
    utils = StringUtils()
    result = utils.contains("SkyPro", "U")
    assert result is False


def test_delete_symbol_positive_char():
    utils = StringUtils()
    result = utils.delete_symbol("SkyPro", "k")
    assert result == "SyPro"


def test_delete_symbol_not_found():
    utils = StringUtils()
    result = utils.delete_symbol("SkyPro", "Z")
    assert result == "SkyPro"
