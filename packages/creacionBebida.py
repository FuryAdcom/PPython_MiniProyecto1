from os import system, name 
from .inicio import inicio
from .clear import clear
from .bebidas import bebidas
from .precioBebida import precioBebida

def creacionBebida(dictionary):
    
    clear()
    inicio()
    numero = len(dictionary)+1
    print('Bebida número {}'.format(numero))

    dictionary[numero] = {}

    dictionary[numero]['fresco'] = bebidas()

    dictionary[numero]['price'] = precioBebida(dictionary[numero])

    print('Usted seleccionó una Bebida de '.join(dictionary[numero]['fresco']))
    print('\nSubtotal a pagar por la Bebida: ',dictionary[numero]['price'])

    return dictionary