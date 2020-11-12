from .creacionHelado import creacionHelado
from .creacionBebida import creacionBebida
from .factura import factura

def continuar(dictionary):
    dicbebida = {}
    dichelado = {}
    
    print('****************************')
    opt = input('¿Desea continuar [s/n]?: ').lower()

    if opt not in ['n','s']:
        print('=> Debe introducir una opción correcta.')
        continuar(dictionary)
    else:
        if opt == 's':
            from .creacion import creacion as create
            
            create(dictionary)
        else:
            total = 0
            for sandwich in dictionary:
                total += dictionary[sandwich]['price']
            print('****************************')
            print('El pedido tiene un total de {} sandwich(es) por un monto de {}'.format(len(dictionary), total))

            cont = 0

            while cont == 0:
                op = input('\nDesea agregar una bebida o un helado a su compra: \nHelado (h)\nBebida (b)\nSalir (Enter)\n').lower()

                if op == 'h':
                   
                    dichelado = creacionHelado(dichelado)
                    
                    print('****************************')
                    opt2 = input('¿Desea continuar [s/n]?: ').lower()

                    v = 0
                    while v == 0:
                        if opt2 == 's':
                            cont = 0
                            v = 1
                        elif opt2 == 'n':
                            cont = 1
                            v = 1
                        else: 
                            opt2 = input('Debe introducir una opción correcta.').lower()
                    
                elif op == 'b':
        
                    dicbebida = creacionBebida(dicbebida)

                    print('****************************')
                    opt2 = input('¿Desea continuar [s/n]?: ').lower()

                    v = 0
                    while v == 0:
                        if opt2 == 's':
                            cont = 0
                            v = 1
                        elif opt2 == 'n':
                            cont = 1
                            v = 1
                        else: 
                            opt2 = input('Debe introducir una opción correcta.').lower()
                else:
                    cont = 1

            factura(dictionary, dichelado, dicbebida)

            print('\nGracias por su compra, regrese pronto.')