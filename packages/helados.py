def helados():
    sabores = {
        'ch':'Chocolate',
        'va':'Vainilla',
        'fr':'Fresa',
        'or':'Oreo',
    }
    selechelado = []

    print('\nSabores de helados:\nChocolate (ch)\nVainilla (va)\nFresa (fr)\nOreo (or)')
    opt = input('\nIndique el sabor del helado que desea: ').lower()
    
    if opt != '' and opt not in list(sabores.keys()):
        print("=> Debe seleccionar un sabor de helado correcto.")
        opt = input('Indique sabor: ').lower()
    else:
        if len(selechelado) == 0 and opt != '':
            selechelado.append(sabores[opt])
        else:
            opt = input('Ingrese un sabor para su Helado: ').lower()
            selechelado.append(sabores[opt])
    
    return selechelado