"""Testy czarnoskrzynkowe: ticket_price (BL-1 ... BL-4)."""
import pytest
from sut import ticket_price

# EP – klasy poprawne: jedna typowa wartość z każdej klasy WEJŚCIA
# (uwaga: cena 10.0 dotyczy dwóch różnych grup wieku)
@pytest.mark.parametrize("age, price", [
    pytest.param(4, 0.0, id="free_0_to_6"),
    pytest.param(12, 10.0, id="discount_youth_7_to_18"),
    pytest.param(40, 20.0, id="normal_19_to_64"),
    pytest.param(75, 10.0, id="discount_senior_65_to_120"),
])
def test_ep_valid_classes(age, price):
    assert ticket_price(age) == price


# EP – klasy niepoprawne (wartość spoza zakresu 0–120 -> ValueError)
@pytest.mark.parametrize("age", [
    pytest.param(-5, id="negative"),
    pytest.param(130, id="above_120"),
])
def test_ep_out_of_range(age):
    with pytest.raises(ValueError):
        ticket_price(age)


# EP – klasy niepoprawne (typ inny niż int -> TypeError)
@pytest.mark.parametrize("age", [
    pytest.param(18.5, id="float"),
    pytest.param("30", id="str"),
    pytest.param(None, id="none"),
    pytest.param(True, id="bool_true"),
    pytest.param(False, id="bool_false"),
])
def test_ep_wrong_type(age):
    with pytest.raises(TypeError):
        ticket_price(age)


# AWB 2-punktowa (2p): wartości poprawne na brzegach klas i dziedziny
@pytest.mark.parametrize("age, price", [
    pytest.param(0, 0.0, id="min_0"),
    pytest.param(6, 0.0, id="free_end_6"),
    pytest.param(7, 10.0, id="youth_start_7"),
    pytest.param(18, 10.0, id="youth_end_18"),
    pytest.param(19, 20.0, id="normal_start_19"),
    pytest.param(64, 20.0, id="normal_end_64"),
    pytest.param(65, 10.0, id="senior_start_65"),
    pytest.param(120, 10.0, id="max_120", marks=pytest.mark.xfail(reason="DEF-05", strict=True)),
])
def test_bva_2p(age, price):
    assert ticket_price(age) == price


# AWB 2-punktowa poza dziedziną: skrajne brzegi poza zakresem (-1 i 121 -> ValueError)
@pytest.mark.parametrize("age", [
    pytest.param(-1, id="below_min_minus_1"),
    pytest.param(121, id="above_max_121"),
])
def test_bva_2p_out_of_domain(age):
    with pytest.raises(ValueError):
        ticket_price(age)


# AWB 3-punktowa – dodatkowe wartości (bez powtarzania punktów z 2p)
@pytest.mark.parametrize("age, price", [
    pytest.param(1, 0.0, id="after_min_1"),
    pytest.param(5, 0.0, id="before_free_end_5"),
    pytest.param(17, 10.0, id="before_youth_end_17"),
    pytest.param(63, 20.0, id="before_normal_end_63"),
    pytest.param(119, 10.0, id="before_max_119", marks=pytest.mark.xfail(reason="DEF-05", strict=True)),
])
def test_bva_3p_extra(age, price):
    assert ticket_price(age) == price