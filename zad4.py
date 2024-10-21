def wyswietl_co_drugi_element(lista_liczb):
    for i in range(0, len(lista_liczb), 2):
        print(lista_liczb[i])

liczby = list(range(10))
wyswietl_co_drugi_element(liczby)
