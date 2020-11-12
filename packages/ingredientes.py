def ingredientes():
    ingredientes = {
        'ja':'Jamón',
        'ch':'Champiñones',
        'pi':'Pimentón',
        'dq':'Doble Queso',
        'ac':'Aceitunas',
        'pp':'Pepperoni',
        'sa':'Salchichón'
    }
    seleccionados = []

    print('\nIngredientes:\nJamón (ja)\nChampiñones (ch)\nPimentón (pi)\nDoble Queso (dq)\nAceitunas (ac)\nPepperoni (pp)\nSalchichón (sa)\n')
    opt = input('Indique ingrediente (enter para terminar): ').lower()
    
    if opt != '' and opt not in list(ingredientes.keys()):
        print("=> Debe seleccionar un ingrediente correcto o presione 'Enter' para finalizar.")
        opt = input('Indique ingrediente (enter para terminar): ').lower()
    else:
        while opt != '' and opt in list(ingredientes.keys()):
            if ingredientes[opt] not in seleccionados: seleccionados.append(ingredientes[opt])
            else: print('El ingrediente ya se ha seleccionado.')
            opt = input('Indique ingrediente (enter para terminar): ').lower()

        if len(seleccionados) == 0:
            seleccionados.append('Queso')
        
    return seleccionados