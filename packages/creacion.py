from os import system, name 
from .inicio import inicio
from .clear import clear
from .size import size
from .ingredientes import ingredientes
from .precio import precio

def creacion(dictionary):
    from .continuar import continuar
    
    inicio()
    numero = len(dictionary)+1
    print('Sandwich número {}'.format(numero))

    dictionary[numero] = {}
    dictionary[numero]['size'] = size()

    clear()
    inicio()
    print('Sandwich número {}'.format(numero))
    print('\nTamaños: Triple ( t ) Doble ( d ) Individual ( i ): '+dictionary[numero]['size'])
    dictionary[numero]['ingre'] = ingredientes()

    dictionary[numero]['price'] = precio(dictionary[numero])

    print('Usted seleccionó un sándwich {} con {}'.format(dictionary[numero]['size'], ', '.join(dictionary[numero]['ingre'])))
    print('\nSubtotal a pagar por un sándwich {}: {}'.format(dictionary[numero]['size'], dictionary[numero]['price']))

    continuar(dictionary)