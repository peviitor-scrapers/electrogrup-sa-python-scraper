"""Unit tests for county resolution."""

from scraper.get_county import get_county


def test_direct_mapping():
    assert get_county("Cluj-Napoca") == "Cluj"
    assert get_county("Bucuresti") == "Bucuresti"
    assert get_county("Timisoara") == "Timis"
    assert get_county("Iasi") == "Iasi"


def test_alias_mapping():
    assert get_county("Bucharest") == "Bucuresti"
    assert get_county("cluj") == "Cluj"
    assert get_county("Brasov") == "Brasov"
    assert get_county("Ploiesti") == "Prahova"


def test_case_insensitive():
    assert get_county("cluj-napoca") == "Cluj"
    assert get_county("BUcuresti") == "Bucuresti"


def test_unknown_city():
    assert get_county("Atlantis") is None


def test_empty_input():
    assert get_county(None) is None
    assert get_county("") is None
