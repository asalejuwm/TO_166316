"""Testy czarnoskrzynkowe: parking_fee (PK-1 ... PK-5)."""
import pytest

from sut import parking_fee


# EP – klasy poprawne (uwzględniające klasy wyjść: 0.0, 5.0, 10.0, 15.0, 20.0)
@pytest.mark.parametrize("minutes, fee", [
    pytest.param(10, 0.0, id="free_0_to_15"),
    pytest.param(40, 5.0, id="hour_1_16_to_60"),
    pytest.param(90, 10.0, id="hour_2_61_to_120"),
    pytest.param(150, 15.0, id="hour_3_121_to_180"),
    pytest.param(600, 20.0, id="daily_181_to_1440"),
])
def test_ep_valid_classes(minutes, fee):
    assert parking_fee(minutes) == fee


# EP – klasy niepoprawne (wartość spoza zakresu 0–1440)
@pytest.mark.parametrize("minutes", [
    pytest.param(-10, id="negative"),
    pytest.param(1500, id="above_1440"),
])
def test_ep_out_of_range(minutes):
    with pytest.raises(ValueError):
        parking_fee(minutes)


# EP – klasy niepoprawne (typ inny niż int)
@pytest.mark.parametrize("minutes", [
    pytest.param(30.5, id="float"),
    pytest.param("60", id="str"),
    pytest.param(None, id="none"),
    pytest.param(True, id="bool_true"),
    pytest.param(False, id="bool_false"),
])
def test_ep_wrong_type(minutes):
    with pytest.raises(TypeError):
        parking_fee(minutes)


# AWB 2-punktowa (2p): wartości poprawne na granicach klas wejścia i wyjść
@pytest.mark.parametrize("minutes, fee", [
    pytest.param(0, 0.0, id="min_0"),
    pytest.param(15, 0.0, id="free_end_15"),
    pytest.param(16, 5.0, id="rate_5_start_16"),
    pytest.param(60, 5.0, id="rate_5_end_60"),
    pytest.param(61, 10.0, id="rate_10_start_61"),
    pytest.param(120, 10.0, id="rate_10_end_120"),
    pytest.param(121, 15.0, id="rate_15_start_121"),
    pytest.param(180, 15.0, id="rate_15_end_180"),
    pytest.param(181, 20.0, id="daily_start_181"),
    pytest.param(1440, 20.0, id="max_1440"),
])
def test_bva_2p(minutes, fee):
    assert parking_fee(minutes) == fee


# AWB 3-punktowa – dodatkowe wartości (bez powtarzania punktów z 2p)
@pytest.mark.parametrize("minutes, fee", [
    pytest.param(1, 0.0, id="after_min_1", marks=pytest.mark.xfail(reason="DEF-03", strict=True)),
    pytest.param(14, 0.0, id="before_free_end_14"),
    pytest.param(59, 5.0, id="before_rate_5_end_59"),
    pytest.param(119, 10.0, id="before_rate_10_end_119"),
    pytest.param(179, 15.0, id="before_rate_15_end_179"),
    pytest.param(1439, 20.0, id="before_max_1439"),
])
def test_bva_3p_extra(minutes, fee):
    assert parking_fee(minutes) == fee


# Wartości brzegowe poza zakresem (-1 i 1441) zgłaszające ValueError
@pytest.mark.parametrize("minutes", [
    pytest.param(-1, id="below_min_minus_1"),
    pytest.param(1441, id="above_max_1441"),
])
def test_bva_out_of_range(minutes):
    with pytest.raises(ValueError):
        parking_fee(minutes)