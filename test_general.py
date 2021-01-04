from eu_country_codes import COUNTRY_CODES


def test_germany():
    assert "DE" in COUNTRY_CODES


def test_code_from_outside_eu():
    assert "ZW" not in COUNTRY_CODES


def test_gb_no_longer_in_eu():
    assert "GB" not in COUNTRY_CODES


def test_number_of_eu_countries():
    assert len(COUNTRY_CODES) == 27
