def wyswietl_parzyste(lista_liczb):
    for liczba in lista_liczb:
        if liczba % 2 == 0:
            print(liczba)

liczby = list(range(10))
wyswietl_parzyste(liczby)
