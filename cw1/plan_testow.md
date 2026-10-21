# Plan testów – szablon (skrócony, wg ISO/IEC/IEEE 29119-3)

> Wypełnij pola w nawiasach `<…>`. Plan skrócony – na ćwiczeniach wystarczy 1–2 zdania lub krótka lista w każdym punkcie.
> Usuń komentarze w cudzysłowie blokowym przed oddaniem.

| | |
|---|---|
| Identyfikator planu | `<PT-KinoTO-01>` |
| Wersja / data | `<1.0 / 2026-10-12>` |
| Autor | `<Adam Salej, 166316>` |
| Status | `<do przeglądu>` |

## 1. Kontekst testowania

### 1.1 Przedmiot testów (elementy testowe)
`<KinoTO 1.0, symulator w Excelu>`

### 1.2 Zakres testów
- **W zakresie:** `<Wszystkie wymagania REQ-FRM i REQ-CEN, pokryte jak najmniejszą ilością przypadków testowych>`
- **Poza zakresem:** `<>`

### 1.3 Podstawa testów
`<specyfikacja_KinoTO.md v1.0>`

### 1.4 Założenia i ograniczenia
`<czas: 1 zajęcia; system dostępny tylko jako symulator; brak dostępu do logiki (czarna skrzynka)>`

### 1.5 Interesariusze
`<prowadzący (klient)>`

## 2. Komunikacja
`<Wszystkie pliki zawarte w repozytorium na Githubie, właściwe raporty o defektach znajdują się w pliku "Salej_cw1.xlsx">` 

## 3. Rejestr ryzyk

| ID | Ryzyko (produktowe / projektowe) | Prawdopodobieństwo (1–3) | Wpływ (1–3) | Poziom (P×W) | Działanie ograniczające |
|---|---|---|---|---|---|
| R1 | `<Produktowe>` | 1 | 3 | 3 | Niepoprawnie naliczane ceny |
| R2 | `<Produktowe>` | 1 | 2 | 2 | Nieprawidłowości przy wartościach granicznych lub innych parametrach danych wejściowych |
| R3 | `<Projektowe>` | 2 | 1 | 2 | Zbyt krótki czas na wykonanie |

## 4. Strategia testów

### 4.1 Poziomy i typy testów
`<testy systemowe, funkcjonalne, czarnoskrzynkowe; manualne na tym etapie>`

### 4.2 Techniki projektowania testów
`<podział na klasy równoważności, analiza wartości brzegowych, lista kontrolna, testowanie eksploracyjne>`

### 4.3 Kryteria wejścia
`<dostępne środowisko, zatwierdzona specyfikacja>`

### 4.4 Kryteria wyjścia (ukończenia)
`<100% przypadków o priorytecie Wysoki wykonanych, każde wymaganie pokryte przynjamniej 1 przypadkiem, brak otwartych defektów krytycznych>`

### 4.5 Kryteria zawieszenia i wznowienia
`<zawieszenie, gdy strona nie działa / blokujący defekt; wznowienie po naprawie>`

### 4.6 Dane testowe i środowisko
`<LibreOffice Calc, Symulator_KinoTO.xlsx, czyszczenie pól przed każdym testem>`

### 4.7 Retesty i testy regresji
`<>`

### 4.8 Metryki
`<liczba wykonanych / zaliczonych przypadków, liczba defektów wg ważności, pokrycie wymagań>`

### 4.9 Produkty testowania (testalia)
`<plan testów, arkusz przypadków, macierz śledzenia, raporty defektów, lista kontrolna, raport z wykonania>`

## 5. Działania testowe i harmonogram

| Działanie | Kto | Termin / czas | Produkt |
|---|---|---|---|
| `<analiza specyfikacji>`| Adam Salej | 2026-10-07 | Przegląd specyfikacji |
| `<projektowanie przypadków>` | Adam Salej | 2026-10-07 | Przypadki testowe |
| `<wykonanie / sesja eksploracyjna>` | Adam Salej | 2026-10-07 - 2026-10-12 | Sesja eksploracyjna |
| `<raportowanie>` | Adam Salej | 2026-10-12 | Macierz śledzenia, Raporty defektów, Lista kontrolna, Raport z wykonania |

## 6. Role i odpowiedzialności
`<Planowanie, projektowanie, wykonanie - Adam Salej, Zatwierdzenie - Prowadzący>`

## 7. Zatwierdzenie

| Rola | Imię i nazwisko | Data | Podpis |
|---|---|---|---|
| Autor | Adam Salej | 2026-10-12 | |
| Zatwierdzający | | | |
