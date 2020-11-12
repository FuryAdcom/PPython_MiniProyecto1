def precioHelado(sabores):
    shelado = 0

    helado= {
        'Chocolate': 250,
        'Vainilla': 240,
        'Fresa': 245,
        'Oreo': 255,
    }

    for ing in sabores['sabor']:
        shelado += helado[ing]

    return shelado