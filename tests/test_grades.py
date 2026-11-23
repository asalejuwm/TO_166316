"""Testy czarnoskrzynkowe: grade_from_percent (OC-1 ... OC-4)."""
import pytest
from sut import grade_from_percent


# EP – klasy poprawne: jedna typowa wartość z każdej klasy
@pytest.mark.parametrize("percent, grade", [
    pytest.param(25, 2.0, id="fail"),
    pytest.param(55, 3.0, id="satisfactory"),
    pytest.param(65, 3.5, id="satisfactory_plus"),
    pytest.param(75, 4.0, id="good"),
    pytest.param(85, 4.5, id="good_plus"),
    pytest.param(95, 5.0, id="very_good"),
])
def test_ep_valid_classes(percent, grade):
    assert grade_from_percent(percent) == grade


# EP – klasy niepoprawne (wartość): jeden test = jedna klasa
@pytest.mark.parametrize("percent", [
    pytest.param(-10, id="negative"),
    pytest.param(120, id="above_100"),
])
def test_ep_out_of_range(percent):
    with pytest.raises(ValueError):
        grade_from_percent(percent)


# EP – klasy niepoprawne (typ): argumenty innego typu niż int (OC-4)
@pytest.mark.parametrize("percent", [
    pytest.param(75.5, id="float", marks=pytest.mark.xfail(reason="DEF-02", strict=True)),
    pytest.param("75", id="str", marks=pytest.mark.xfail(reason="DEF-02", strict=True)),
    pytest.param(None, id="none"),
    pytest.param(True, id="bool_true", marks=pytest.mark.xfail(reason="DEF-02", strict=True)),
    pytest.param(False, id="bool_false", marks=pytest.mark.xfail(reason="DEF-02", strict=True)),
])
def test_ep_wrong_type(percent):
    with pytest.raises(TypeError):
        grade_from_percent(percent)


# AWB 2-punktowa (2p): wartości poprawne na granicach / progach
@pytest.mark.parametrize("percent, grade", [
    pytest.param(0, 2.0, id="min_0"),
    pytest.param(50, 2.0, id="max_fail_50"),
    pytest.param(51, 3.0, id="min_satisfactory_51"),
    pytest.param(60, 3.0, id="max_satisfactory_60"),
    pytest.param(61, 3.5, id="min_satisfactory_plus_61"),
    pytest.param(70, 3.5, id="max_satisfactory_plus_70"),
    pytest.param(71, 4.0, id="min_good_71"),
    pytest.param(80, 4.0, id="max_good_80"),
    pytest.param(81, 4.5, id="min_good_plus_81"),
    pytest.param(90, 4.5, id="max_good_plus_90", marks=pytest.mark.xfail(reason="DEF-01", strict=True)),
    pytest.param(91, 5.0, id="min_very_good_91"),
    pytest.param(100, 5.0, id="max_100"),
])
def test_bva_2p(percent, grade):
    assert grade_from_percent(percent) == grade


# AWB 3-punktowa – dodatkowe wartości (bez powtarzania punktów z 2p)
@pytest.mark.parametrize("percent, grade", [
    pytest.param(1, 2.0, id="after_min_1"),
    pytest.param(49, 2.0, id="before_50"),
    pytest.param(52, 3.0, id="after_51"),
    pytest.param(59, 3.0, id="before_60"),
    pytest.param(62, 3.5, id="after_61"),
    pytest.param(69, 3.5, id="before_70"),
    pytest.param(72, 4.0, id="after_71"),
    pytest.param(79, 4.0, id="before_80"),
    pytest.param(82, 4.5, id="after_81"),
    pytest.param(89, 4.5, id="before_90"),
    pytest.param(92, 5.0, id="after_91"),
    pytest.param(99, 5.0, id="before_max_99"),
])
def test_bva_3p_extra(percent, grade):
    assert grade_from_percent(percent) == grade


# Wartości brzegowe poza zakresem (-1 i 101) zgłaszające ValueError
@pytest.mark.parametrize("percent", [
    pytest.param(-1, id="below_min_minus_1"),
    pytest.param(101, id="above_max_101"),
])
def test_bva_out_of_range(percent):
    with pytest.raises(ValueError):
        grade_from_percent(percent)