def precio(sandwich):
    suma = 0
    precios = {
        'Triple': 580,
        'Doble': 430,
        'Individual': 280,
        'Jamón': 40,
        'Champiñones': 35,
        'Pimentón': 30,
        'Doble Queso': 40,
        'Aceitunas': 57.5,
        'Pepperoni': 38.5,
        'Salchichón': 62.5,
    }

    suma += precios[sandwich['size']]
    if 'Queso' not in sandwich['ingre']:
        for ing in sandwich['ingre']:
            suma += precios[ing]

    return suma