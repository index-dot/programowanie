def przetworz_listy(lista1, lista2):
    polaczona_lista = list(set(lista1 + lista2))

    lista_potegi = [x ** 3 for x in polaczona_lista]

    return lista_potegi

lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]

wynik = przetworz_listy(lista1, lista2)

print(wynik)
