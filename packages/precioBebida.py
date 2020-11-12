def precioBebida(drink):
    sbebida = 0

    refresco= {
        'Cocacola': 150,
        'Pepsi': 140,
        '7up': 145,
        'Chinoto': 155,
        'Golden': 155,
        'Malta': 100,
    }
    
    for i in drink['fresco']:
        sbebida += refresco[i]

    return sbebida