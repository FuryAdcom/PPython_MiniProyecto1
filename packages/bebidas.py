def bebidas():
    marcas = {
        'co':'Cocacola',
        'pe':'Pepsi',
        'se':'7up',
        'ch':'Chinoto',
        'go':'Golden',
        'ma':'Malta',
    }
    selecbebidas = []

    print('\nSabores de Bebidas:\nCocacola (co)\nPepsi (pe)\n7up (se)\nChinoto (ch)\nGolden (go)\nMalta (ma)')
    opt = input('\nIndique su bebida: ').lower()
    
    if opt != '' and opt not in list(marcas.keys()):
        print("=> Debe seleccionar una bebida correcto.")
        opt = input('Indique marca: ').lower()
    else:
        if len(selecbebidas) == 0 and opt != '':
            selecbebidas.append(marcas[opt])
        else:
            opt = input('Ingrese un bebida: ').lower()
            selecbebidas.append(marcas[opt])
    
    return selecbebidas