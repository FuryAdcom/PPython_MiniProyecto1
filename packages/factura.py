from .clear import clear
from .inicio import inicio

def factura(sand, helado, fres):
    total = 0
    clear()
    inicio()

    print('Su compra fue de los siguientes productos: \n')

    for pan in sand:
        print('Sandwich numero:',pan, ', '.join(sand[pan]['ingre']))
        total += sand[pan]['price']

    for ice in helado:
        print('Helado numero:',ice, ' de: '.join(helado[ice]['sabor']))
        total += helado[ice]['price']

    for rf in fres:
        print('Bebida numero:',rf, ' de: '.join(fres[rf]['fresco']))
        total += fres[rf]['price']
    
    print('\nEl Total de su factura es pagar:', total) 
    

