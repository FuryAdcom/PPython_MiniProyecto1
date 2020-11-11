from os import system, name 
from .inicio import inicio
from .clear import clear
from .helados import helados
from .precioHelado import precioHelado

def creacionHelado(dictionary):
    
    clear()
    inicio()
    numero = len(dictionary)+1
    print('Helado número {}'.format(numero))

    dictionary[numero] = {}

    dictionary[numero]['sabor'] = helados()

    dictionary[numero]['price'] = precioHelado(dictionary[numero])

    print('Usted seleccionó un Helado con '.join(dictionary[numero]['sabor']))
    print('\nSubtotal a pagar por el Helado: ',dictionary[numero]['price'])

    return dictionary