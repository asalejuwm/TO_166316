"""Testy czarnoskrzynkowe: validate_password (HS-1 ... HS-4)."""
import pytest
from sut import validate_password

def password_of_length(n):
    """Hasło z liter i cyfr o długości n, np. 5 -> 'a1a1a'."""
    return ("a1" * n)[:n]


def test_example_valid_password():
    assert validate_password("haslo123") is True


def test_example_wrong_type():
    with pytest.raises(TypeError):
        validate_password(None)


# EP – klasy poprawne (HS-3, HS-4: polskie litery, znaki specjalne, spacje)
@pytest.mark.parametrize("password", [
    pytest.param("haslo123", id="basic_letters_digits"),
    pytest.param("Żółw1234", id="polish_letters"),
    pytest.param("Haslo#123!", id="special_chars", marks=pytest.mark.xfail(reason="DEF-04", strict=True)),
    pytest.param("Haslo 123", id="spaces", marks=pytest.mark.xfail(reason="DEF-04", strict=True)),
    pytest.param("Zażółć123 !@#", id="polish_special_space", marks=pytest.mark.xfail(reason="DEF-04", strict=True)),
])
def test_ep_valid(password):
    assert validate_password(password) is True


# EP – klasy niepoprawne (zwracające False): każda klasa w osobnym pytest.param
@pytest.mark.parametrize("password", [
    pytest.param("12345678", id="no_letter"),
    pytest.param("haslobezcyfry", id="no_digit"),
    pytest.param("haslo1", id="too_short"),
    pytest.param("bardzo_dlugie_haslo_12345", id="too_long"),
    pytest.param("", id="empty_string"),
])
def test_ep_invalid(password):
    assert validate_password(password) is False


# EP – niepoprawny typ argumentu (HS-1 -> TypeError)
@pytest.mark.parametrize("password", [
    pytest.param(None, id="none"),
    pytest.param(12345678, id="int"),
    pytest.param(True, id="bool"),
    pytest.param(["a", "1"], id="list"),
])
def test_ep_wrong_type(password):
    with pytest.raises(TypeError):
        validate_password(password)


# AWB długości (2p) – wartości na granicach długości (z użyciem password_of_length)
@pytest.mark.parametrize("length, expected", [
    pytest.param(0, False, id="len_0_empty"),
    pytest.param(2, False, id="len_2_short"),
    pytest.param(7, False, id="len_7_below_min"),
    pytest.param(8, True, id="len_8_min_valid"),
    pytest.param(20, True, id="len_20_max_valid"),
    pytest.param(21, False, id="len_21_above_max"),
])
def test_bva_length_2p(length, expected):
    assert validate_password(password_of_length(length)) is expected


# AWB długości (3p – dodatkowo): punkty dodatkowe bez powtarzania z 2p
@pytest.mark.parametrize("length, expected", [
    pytest.param(5, False, id="len_5_extra_short"),
    pytest.param(9, True, id="len_9_extra_above_min"),
    pytest.param(19, True, id="len_19_extra_below_max"),
])
def test_bva_length_3p_extra(length, expected):
    assert validate_password(password_of_length(length)) is expected