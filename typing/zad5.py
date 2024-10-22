def czy_zawiera(lista, liczba):
    return liczba in lista

lista_przykladowa = [1, 2, 3, 4, 5]
liczba_do_sprawdzenia = 3

wynik = czy_zawiera(lista_przykladowa, liczba_do_sprawdzenia)

print(wynik)
