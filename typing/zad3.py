def czy_parzysta(liczba):
    return liczba % 2 == 0

liczba = 5
wynik = czy_parzysta(liczba)

if wynik:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
