"""
40. Leer 10 números enteros, almacenarlos en un vector y determinar cuántos
números de los almacenados en dicho vector terminan en 15.
"""
import re

def main():

    lista = []

    while True:
        try:
            for j in range(10):
                n = j+1
                num = int(input(f'{n}. Ingrese un numero: '))
                lista.append(str(num))
                if len(lista) == 10:
                    break
            break
        except ValueError:
            lista = []
            print('Valor incorrecto.')

    lista_end_15 = []

    for q in lista:
        if q.endswith('15'):
            lista_end_15.append(q)

    cant_end_15 = len(lista_end_15)

    print(f'\nHay {cant_end_15} numeros en el vector acabados en 15.')

if __name__ == "__main__":
    main()