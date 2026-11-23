# Analiza czarnoskrzynkowa – ćwiczenia 2 (`analiza_cw2.md`)

Analiza obejmuje cztery funkcje modułu `sut`:
- `grade_from_percent(percent)` (`OC-1` … `OC-4`)
- `parking_fee(minutes)` (`PK-1` … `PK-5`)
- `validate_password(password)` (`HS-1` … `HS-4`)
- `ticket_price(age)` (`BL-1` … `BL-4`)

---

## B2. Podział na klasy równoważności (EP)

### Uwaga dotycząca klas niepoprawnych typu (m.in. `OC-4`, `PK-5`, `BL-4`, `HS-1`)
W Pythonie `bool` jest podklasą `int` (`isinstance(True, int) == True`), dlatego szczególnie warto wyróżnić osobne klasy dla:
- `bool` (`True`, `False`),
- `float` (np. `50.5`),
- `str` (np. `"75"`),
- `None` (`None`) – oraz ewentualnie innych typów (np. `list`, `dict`).

---

### 1. `grade_from_percent(percent)`

| Klasa | Opis | Rodzaj | Wartość | Oczekiwany |
|-------|------|--------|---------|------------|
| `OC-P1` | Procent w zakresie `0–50` (ocena niedostateczna) | poprawna (wejście) | `25` | `2.0` |
| `OC-P2` | Procent w zakresie `51–60` (ocena dostateczna) | poprawna (wejście) | `55` | `3.0` |
| `OC-P3` | Procent w zakresie `61–70` (ocena dostateczna plus) | poprawna (wejście) | `65` | `3.5` |
| `OC-P4` | Procent w zakresie `71–80` (ocena dobry) | poprawna (wejście) | `75` | `4.0` |
| `OC-P5` | Procent w zakresie `81–90` (ocena dobry plus) | poprawna (wejście) | `85` | `4.5` |
| `OC-P6` | Procent w zakresie `91–100` (ocena bardzo dobry) | poprawna (wejście) | `95` | `5.0` |
| `OC-N1` | Liczba `int` poniżej `0` (`< 0`) | niepoprawna (wartość) | `-10` | `ValueError` |
| `OC-N2` | Liczba `int` powyżej `100` (`> 100`) | niepoprawna (wartość) | `120` | `ValueError` |
| `OC-N3` | Typ `bool` (`True` / `False`) | niepoprawna (typ) | `True` | `TypeError` |
| `OC-N4` | Typ `float` | niepoprawna (typ) | `75.5` | `TypeError` |
| `OC-N5` | Typ `str` | niepoprawna (typ) | `"75"` | `TypeError` |
| `OC-N6` | Typ `NoneType` (`None`) | niepoprawna (typ) | `None` | `TypeError` |

---

### 2. `parking_fee(minutes)`

#### Klasy wejścia oraz klasy niepoprawne
| Klasa | Opis | Rodzaj | Wartość | Oczekiwany |
|-------|------|--------|---------|------------|
| `PK-P1` | Postój `0–15` min (bezpłatny) | poprawna (wejście) | `10` | `0.0` |
| `PK-P2` | Postój `16–60` min (1. rozpoczęta godzina) | poprawna (wejście) | `40` | `5.0` |
| `PK-P3` | Postój `61–120` min (2. rozpoczęta godzina) | poprawna (wejście) | `90` | `10.0` |
| `PK-P4` | Postój `121–180` min (3. rozpoczęta godzina) | poprawna (wejście) | `150` | `15.0` |
| `PK-P5` | Postój `181–1440` min (opłata dobowa) | poprawna (wejście) | `500` | `20.0` |
| `PK-N1` | Liczba `int` poniżej `0` (`< 0`) | niepoprawna (wartość) | `-5` | `ValueError` |
| `PK-N2` | Liczba `int` powyżej `1440` (`> 1440`) | niepoprawna (wartość) | `1500` | `ValueError` |
| `PK-N3` | Typ `bool` (`True` / `False`) | niepoprawna (typ) | `False` | `TypeError` |
| `PK-N4` | Typ `float` | niepoprawna (typ) | `30.5` | `TypeError` |
| `PK-N5` | Typ `str` | niepoprawna (typ) | `"60"` | `TypeError` |
| `PK-N6` | Typ `NoneType` (`None`) | niepoprawna (typ) | `None` | `TypeError` |

#### Klasy wyjścia (opłata w zł: `0`, `5`, `10`, `15`, `20` zł)
| Klasa wyjścia | Opis opłaty | Odpowiadające klasy wejścia | Przykładowa wartość wejścia | Oczekiwany |
|---------------|-------------|-----------------------------|-----------------------------|------------|
| `PK-W0` | Opłata `0.0` zł | `PK-P1` (`0–15` min) | `10` | `0.0` |
| `PK-W5` | Opłata `5.0` zł | `PK-P2` (`16–60` min) | `40` | `5.0` |
| `PK-W10` | Opłata `10.0` zł | `PK-P3` (`61–120` min) | `90` | `10.0` |
| `PK-W15` | Opłata `15.0` zł | `PK-P4` (`121–180` min) | `150` | `15.0` |
| `PK-W20` | Opłata `20.0` zł | `PK-P5` (`181–1440` min) | `500` | `20.0` |

---

### 3. `validate_password(password)`

| Klasa | Opis | Rodzaj | Wartość | Oczekiwany |
|-------|------|--------|---------|------------|
| `HS-P1` | Długość poprawna (`8–20` znaków), zawiera literę i cyfrę | poprawna (długość/skład) | `"haslo123"` | `True` |
| `HS-P2` | Skład: litery (w tym polskie znaki, np. `ą`, `Ż`) i cyfry | poprawna (skład) | `"Żółw1234"` | `True` |
| `HS-P3` | Skład: litery, cyfry oraz inne znaki (specjalne, spacje, wg `HS-4`) | poprawna (inne znaki) | `"Haslo 123!@#"` | `True` |
| `HS-N1` | Długość za krótka (`0–7` znaków, w tym pusty napis `""`) | niepoprawna (długość) | `"haslo1"` | `False` |
| `HS-N2` | Długość za długa (`> 20` znaków) | niepoprawna (długość) | `"bardzo_dlugie_haslo_12345"` | `False` |
| `HS-N3` | Brak litery (np. same cyfry i/lub znaki specjalne, dł. `8–20`) | niepoprawna (skład) | `"12345678"` | `False` |
| `HS-N4` | Brak cyfry (np. same litery i/lub znaki specjalne, dł. `8–20`) | niepoprawna (skład) | `"haslobezcyfry"` | `False` |
| `HS-N5` | Typ `NoneType` (`None`) | niepoprawna (typ) | `None` | `TypeError` |
| `HS-N6` | Typ `int` | niepoprawna (typ) | `12345678` | `TypeError` |
| `HS-N7` | Typ `bool` | niepoprawna (typ) | `True` | `TypeError` |
| `HS-N8` | Typ `list` | niepoprawna (typ) | `["a", "1"]` | `TypeError` |

---

### 4. `ticket_price(age)`

#### Klasy wejścia oraz klasy niepoprawne
| Klasa | Opis | Rodzaj | Wartość | Oczekiwany |
|-------|------|--------|---------|------------|
| `BL-P1` | Wiek `0–6` lat (bilet bezpłatny) | poprawna (wejście) | `4` | `0.0` |
| `BL-P2` | Wiek `7–18` lat (bilet ulgowy – dzieci i młodzież) | poprawna (wejście) | `12` | `10.0` |
| `BL-P3` | Wiek `19–64` lat (bilet normalny) | poprawna (wejście) | `30` | `20.0` |
| `BL-P4` | Wiek `65–120` lat (bilet ulgowy – seniorzy) | poprawna (wejście) | `70` | `10.0` |
| `BL-N1` | Liczba `int` poniżej `0` (`< 0`) | niepoprawna (wartość) | `-3` | `ValueError` |
| `BL-N2` | Liczba `int` powyżej `120` (`> 120`) | niepoprawna (wartość) | `130` | `ValueError` |
| `BL-N3` | Typ `bool` (`True` / `False`) | niepoprawna (typ) | `True` | `TypeError` |
| `BL-N4` | Typ `float` | niepoprawna (typ) | `18.5` | `TypeError` |
| `BL-N5` | Typ `str` | niepoprawna (typ) | `"30"` | `TypeError` |
| `BL-N6` | Typ `NoneType` (`None`) | niepoprawna (typ) | `None` | `TypeError` |

#### Klasy wyjścia (cena biletu: `0`, `10`, `20` zł – `10.0` zł dla dwóch rozłącznych grup wiekowych)
| Klasa wyjścia | Opis ceny | Odpowiadające klasy wejścia | Przykładowa wartość wejścia | Oczekiwany |
|---------------|-----------|-----------------------------|-----------------------------|------------|
| `BL-W0` | Cena `0.0` zł | `BL-P1` (`0–6` lat) | `4` | `0.0` |
| `BL-W10A` | Cena `10.0` zł (grupa 1: `7–18` lat) | `BL-P2` (`7–18` lat) | `12` | `10.0` |
| `BL-W10B` | Cena `10.0` zł (grupa 2: `65–120` lat) | `BL-P4` (`65–120` lat) | `70` | `10.0` |
| `BL-W20` | Cena `20.0` zł | `BL-P3` (`19–64` lat) | `30` | `20.0` |

---

## B3. Analiza wartości brzegowych (AWB)

W analizie brzegowej dla każdego progu/granicy:
- **2p** obejmuje wartości na granicy oraz tuż po drugiej stronie granicy (zgodnie z precyzją),
- **3p – dodatkowo** dorzuca trzeci punkt (np. sąsiedni punkt w głąb przedziału / po drugiej stronie granicy).

---

### 1. `grade_from_percent(percent)` – precyzja: `1 punkt procentowy`

Granice klas wejścia oraz wyjść (`2.0`, `3.0`, `3.5`, `4.0`, `4.5`, `5.0`):
- Dolna granica zakresu: `0` (między `-1` a `0`)
- Próg `50 / 51` (ocena `2.0` / `3.0`)
- Próg `60 / 61` (ocena `3.0` / `3.5`)
- Próg `70 / 71` (ocena `3.5` / `4.0`)
- Próg `80 / 81` (ocena `4.0` / `4.5`)
- Próg `90 / 91` (ocena `4.5` / `5.0`)
- Górna granica zakresu: `100` (między `100` a `101`)

| Granica | 2p | 3p - dodatkowo | Oczekiwane |
|---------|----|----------------|------------|
| Granica `0` (`-1` \| `0`) | `0`, `-1` | `1` | `0` → `2.0`, `-1` → `ValueError`, `1` → `2.0` |
| Granica `50 / 51` (`2.0` \| `3.0`) | `50`, `51` | `49` | `50` → `2.0`, `51` → `3.0`, `49` → `2.0` |
| Granica `60 / 61` (`3.0` \| `3.5`) | `60`, `61` | `62` | `60` → `3.0`, `61` → `3.5`, `62` → `3.5` |
| Granica `70 / 71` (`3.5` \| `4.0`) | `70`, `71` | `69` | `70` → `3.5`, `71` → `4.0`, `69` → `3.5` |
| Granica `80 / 81` (`4.0` \| `4.5`) | `80`, `81` | `82` | `80` → `4.0`, `81` → `4.5`, `82` → `4.5` |
| Granica `90 / 91` (`4.5` \| `5.0`) | `90`, `91` | `89` | `90` → `4.5`, `91` → `5.0`, `89` → `4.5` |
| Granica `100` (`100` \| `101`) | `100`, `101` | `99` | `100` → `5.0`, `101` → `ValueError`, `99` → `5.0` |

- **Liczba elementów pokrycia 2p:** `14` (7 granic × 2 punkty)
- **Liczba elementów pokrycia 3p (łącznie):** `21` (14 z `2p` + 7 dodatkowych)

---

### 2. `parking_fee(minutes)` – precyzja: `1 minuta`

Granice klas wejścia oraz klas wyjść (`0.0`, `5.0`, `10.0`, `15.0`, `20.0`):
- Dolna granica zakresu: `0` (`-1` | `0`)
- Próg `15 / 16` (koniec `0.0` zł / początek `5.0` zł)
- Próg `60 / 61` (koniec `5.0` zł / początek `10.0` zł)
- Próg `120 / 121` (koniec `10.0` zł / początek `15.0` zł)
- Próg `180 / 181` (koniec `15.0` zł / początek `20.0` zł)
- Górna granica zakresu: `1440` (`1440` | `1441`)

| Granica | 2p | 3p - dodatkowo | Oczekiwane |
|---------|----|----------------|------------|
| Granica `0` (`-1` \| `0`) | `0`, `-1` | `1` | `0` → `0.0`, `-1` → `ValueError`, `1` → `0.0` |
| Granica `15 / 16` (`0.0` \| `5.0`) | `15`, `16` | `14` | `15` → `0.0`, `16` → `5.0`, `14` → `0.0` |
| Granica `60 / 61` (`5.0` \| `10.0`) | `60`, `61` | `59` | `60` → `5.0`, `61` → `10.0`, `59` → `5.0` |
| Granica `120 / 121` (`10.0` \| `15.0`) | `120`, `121` | `119` | `120` → `10.0`, `121` → `15.0`, `119` → `10.0` |
| Granica `180 / 181` (`15.0` \| `20.0`) | `180`, `181` | `179` | `180` → `15.0`, `181` → `20.0`, `179` → `15.0` |
| Granica `1440` (`1440` \| `1441`) | `1440`, `1441` | `1439` | `1440` → `20.0`, `1441` → `ValueError`, `1439` → `20.0` |

- **Liczba elementów pokrycia 2p:** `12` (6 granic × 2 punkty)
- **Liczba elementów pokrycia 3p (łącznie):** `18` (12 z `2p` + 6 dodatkowych)

---

### 3. `validate_password(password)` – precyzja: `1 znak` (długość napisu)

Granice długości hasła (`HS-2`):
- Dolny brzeg długości: `0` (napis pusty `""`, poniżej nie ma krótszego napisu `str`)
- Próg długości `7 / 8` (granica zbyt krótkiego hasła i poprawnej długości `8`)
- Próg długości `20 / 21` (granica poprawnej długości `20` i zbyt długiego hasła `> 20`; klasa `> 20` jest otwarta z prawej strony, więc ma jeden próg graniczny `21`)

*(W poniższych przykładach zachowano obecność litery i cyfry, aby testować samą granicę długości).*

| Granica | 2p | 3p - dodatkowo | Oczekiwane |
|---------|----|----------------|------------|
| Granica długości `0` (`""` \| `"a1"`) | `""` (dł. 0), `"a1"` (dł. 2) | `"a1b2c"` (dł. 5) | `""` → `False`, `"a1"` → `False`, `"a1b2c"` → `False` |
| Granica długości `7 / 8` (`7` \| `8` znaków) | `"abcdef1"` (dł. 7), `"abcdef12"` (dł. 8) | `"abcdef123"` (dł. 9) | dł. 7 → `False`, dł. 8 → `True`, dł. 9 → `True` |
| Granica długości `20 / 21` (`20` \| `21` znaków) | `"a123456789012345678b"` (dł. 20), `"a123456789012345678bc"` (dł. 21) | `"a12345678901234567b"` (dł. 19) | dł. 20 → `True`, dł. 21 → `False`, dł. 19 → `True` |

- **Liczba elementów pokrycia 2p:** `6` (3 granice × 2 punkty)
- **Liczba elementów pokrycia 3p (łącznie):** `9` (6 z `2p` + 3 dodatkowe)

---

### 4. `ticket_price(age)` – precyzja: `1 rok`

Granice klas wejścia oraz wyjść (`0.0`, `10.0`, `20.0`):
- Dolna granica wieku: `0` (`-1` | `0`)
- Próg `6 / 7` (bilet bezpłatny `0.0` / ulgowy `10.0`)
- Próg `18 / 19` (ulgowy `10.0` / normalny `20.0`)
- Próg `64 / 65` (normalny `20.0` / ulgowy seniorzy `10.0`)
- Górna granica wieku: `120` (`120` | `121`)

| Granica | 2p | 3p - dodatkowo | Oczekiwane |
|---------|----|----------------|------------|
| Granica `0` (`-1` \| `0`) | `0`, `-1` | `1` | `0` → `0.0`, `-1` → `ValueError`, `1` → `0.0` |
| Granica `6 / 7` (`0.0` \| `10.0`) | `6`, `7` | `5` | `6` → `0.0`, `7` → `10.0`, `5` → `0.0` |
| Granica `18 / 19` (`10.0` \| `20.0`) | `18`, `19` | `17` | `18` → `10.0`, `19` → `20.0`, `17` → `10.0` |
| Granica `64 / 65` (`20.0` \| `10.0`) | `64`, `65` | `63` | `64` → `20.0`, `65` → `10.0`, `63` → `20.0` |
| Granica `120` (`120` \| `121`) | `120`, `121` | `119` | `120` → `10.0`, `121` → `ValueError`, `119` → `10.0` |

- **Liczba elementów pokrycia 2p:** `10` (5 granic × 2 punkty)
- **Liczba elementów pokrycia 3p (łącznie):** `15` (10 z `2p` + 5 dodatkowych)

# Defekty

## DEF-01: `grade_from_percent(percent)` zwraca `5.0` zamiast `4.5` dla `percent = 90`
- **Wymaganie:** `OC-1`, `OC-2` (progi ocen z regulaminu przedmiotu: `81–90` → `4.5`, `91–100` → `5.0`)
- **Kroki:** Wywołaj `grade_from_percent(90)` lub uruchom `python -m pytest -v`.
- **Oczekiwany / rzeczywisty:**
  - **Oczekiwany:** `4.5`
  - **Rzeczywisty:** `5.0` (`AssertionError: assert 5.0 == 4.5`)
- **Test, ważność:** `tests/test_grades.py::test_bva_2p[max_good_plus_90]`; ważność: wysoka

## DEF-02: `grade_from_percent(percent)` nie zgłasza `TypeError` dla argumentów innego typu niż `int`
- **Wymaganie:** `OC-4` (dla argumentu innego typu niż `int`, np. `float`, `str`, `None`, `bool`, funkcja zgłasza `TypeError`)
- **Kroki:** Wywołaj `grade_from_percent(75.5)`, `grade_from_percent("75")`, `grade_from_percent(True)` lub `grade_from_percent(False)` i uruchom `python -m pytest -v`.
- **Oczekiwany / rzeczywisty:**
  - **Oczekiwany:** zgłoszenie wyjątku `TypeError`
  - **Rzeczywisty:** brak zgłoszenia wyjątku `TypeError` (`Failed: DID NOT RAISE TypeError`)
- **Test, ważność:** `tests/test_grades.py::test_ep_wrong_type[float]`, `[str]`, `[bool_true]`, `[bool_false]`; ważność: wysoka

## DEF-03: `parking_fee(minutes)` zwraca `5.0` zamiast `0.0` dla `minutes = 1`
- **Wymaganie:** `PK-2` (postój od `0` do `15` minut włącznie jest bezpłatny – opłata `0.0`)
- **Kroki:** Wywołaj `parking_fee(1)` lub uruchom `python -m pytest -v`.
- **Oczekiwany / rzeczywisty:**
  - **Oczekiwany:** `0.0`
  - **Rzeczywisty:** `5.0` (`AssertionError: assert 5.0 == 0.0`)
- **Test, ważność:** `tests/test_parking.py::test_bva_3p_extra[after_min_1]`; ważność: średnia

## DEF-04: `validate_password(password)` zwraca `False` zamiast `True` dla poprawnych haseł ze znakami specjalnymi i spacjami
- **Wymaganie:** `HS-3`, `HS-4` (hasło dł. `8–20` z literą i cyfrą może zawierać dowolne znaki, w tym znaki specjalne oraz spacje)
- **Kroki:** Wywołaj `validate_password("Haslo#123!")`, `validate_password("Haslo 123")` lub `validate_password("Zażółć123 !@#")` i uruchom `python -m pytest -v`.
- **Oczekiwany / rzeczywisty:**
  - **Oczekiwany:** `True`
  - **Rzeczywisty:** `False` (`AssertionError: assert False is True`)
- **Test, ważność:** `tests/test_passwords.py::test_ep_valid[special_chars]`, `[spaces]`, `[polish_special_space]`; ważność: wysoka

## DEF-05: `ticket_price(age)` zgłasza `ValueError` dla `age = 120` (oraz `age = 119`)
- **Wymaganie:** `BL-1`, `BL-2` (wiek to liczba `int` z zakresu `0–120` włącznie; dla `65–120` cena wynosi `10.0`)
- **Kroki:** Wywołaj `ticket_price(120)` (oraz `ticket_price(119)`) lub uruchom `python -m pytest -v`.
- **Oczekiwany / rzeczywisty:**
  - **Oczekiwany:** `10.0`
  - **Rzeczywisty:** zgłoszenie `ValueError: wiek spoza obsługiwanego zakresu`
- **Test, ważność:** `tests/test_tickets.py::test_bva_2p[max_120]` oraz `tests/test_tickets.py::test_bva_3p_extra[before_max_119]`; ważność: wysoka

# Pokrycie testów (EP, AWB 2p, AWB 3p)

| Funkcja / plik testowy | EP (klasy poprawne, niepoprawne, złe typy) | AWB 2p (brzegi klas/dziedziny) | AWB 3p (2p + punkty sąsiednie/dodatkowe) |
| :--- | :---: | :---: | :---: |
| `grade_from_percent` (`tests/test_grades.py`) | 13 przypadków | 14 przypadków (2p na granicach + brzegi zakresu) | 26 przypadków (14 z 2p + 12 dodatkowych) |
| `parking_fee` (`tests/test_parking.py`) | 12 przypadków | 12 przypadków (2p na granicach + brzegi zakresu) | 18 przypadków (12 z 2p + 6 dodatkowych) |
| `validate_password` (`tests/test_passwords.py`) | 14 przypadków | 6 długości (`0, 2, 7, 8, 20, 21`) | 9 długości (6 z 2p + 3 dodatkowe: `5, 9, 19`) |
| `ticket_price` (`tests/test_tickets.py`) | 11 przypadków | 10 przypadków (2p na granicach + brzegi dziedziny) | 15 przypadków (10 z 2p + 5 dodatkowych) |

# Pytania dodatkowe (zadania samodzielne)

## Hasło o długości 20 znaków z polskimi literami
- **Przykładowe hasło (20 znaków):** `"ŻółćGęślJaźń1234567"` (długość `20`, zawiera polskie litery oraz cyfry).
- **Oczekiwany wynik wg specyfikacji:** `True` — długość `20` mieści się w dopuszczalnym zakresie `8–20` znaków włącznie, a znaki diakrytyczne/polskie litery są traktowane jako poprawne znaki hasła, pod warunkiem obecności co najmniej jednej litery i co najmniej jednej cyfry.

## Minimalny zestaw *Each Choice* dla `validate_password`
W podejściu *Each Choice* każda wyróżniona wartość/klasa parametru musi pojawić się przynajmniej raz w całym zestawie testów:

1. `"Żółć1! a"` (dł. 9) — poprawny `str`, długość w zakresie `8–20`, polskie litery, cyfra, znak specjalny, spacja → oczekiwane `True`.
2. `"12345678"` (dł. 8) — brak litery → oczekiwane `False`.
3. `"abcdefgh"` (dł. 8) — brak cyfry → oczekiwane `False`.
4. `"a1b2c3"` (dł. 6) — długość poniżej minimum (`< 8`) → oczekiwane `False`.
5. `"a1" * 10 + "b"` (dł. 21) — długość powyżej maksimum (`> 20`) → oczekiwane `False`.
6. `None` — typ inny niż `str` → oczekiwany `TypeError`.