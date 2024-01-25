# WSI 2023 LAB7 - Sieci bayesowskie
### Maksym Bieńkowski

# Zawartość archiwum
### `/src`
* `probs.py` - tablice prawdopodobieństw dla wszystkich zmiennych
* `network.py` - sieć bayesowska zaciągająca prawdopodobieństwa z `probs.py`
* `enums.py` - enumy opisujące możliwe stany każdego z elementów sieci
* `experiments.py` - zawiera część zadania związaną z przeprowadzaniem eksperymentów z wykorzystaniem sieci

## Uruchamialne skrypty
### `main.py`
przyjmuje następujące parametry: 
`--weather {1/0}` - pogoda (przyjmuje wartości sprzyjająca i niesprzyjająca)
`--car_maintenance {1/0}` - serwis (przyjmuje wartości aktualny i nieaktualny)
`--battery_age {1/0}` - wiek akumulatora (przyjmuje wartości nowy i stary)
`--electrical_system {1/0}` - układ elektryczny (przyjmuje wartości funkcjonalny i niefunkcjonalny)
`--engine_noise {1/0}` - dźwięk silnika (przyjmuje wartości normalny i nienormalny (głośny))
Dla każdego parametru 0 oznacza "pesymistyczną" wartość, a 1 "optymistyczną"



Wszystkie argumenty mają domyślne wartości, więc możemy uruchomić skrypt poprzez
```shell
`python3 -m main`
```
lub, określając argumenty:
```shell
`python3 -m main --battery_age 0 --engine_noise 0`
```
## Krótki opis rozwiązania
Sieć bayesowska służąca do diagnostyki problemów z uruchamianiem silnika samochodu lub wyznaczania prawdopodobieństwa
jego poprawnego uruchomienia na podstawie kilku czynników, m. in stanu układu elektrycznego, pogody czy dźwięku 
wydawanego przez silnik. 

Diagram sieci:

![Diagram sieci](diagram_sieci.png)

Po więcej szczegółów zapraszam do sprawozdania.
