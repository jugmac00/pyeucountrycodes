from eu_country_codes import COUNTRY_CODES


def test_germany():
    assert "DE" in COUNTRY_CODES


def test_code_from_outside_eu():
    assert "ZW" not in COUNTRY_CODES


def test_brexit():
    assert "GB" not in COUNTRY_CODES
