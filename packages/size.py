def size():
    sizes = {
        't':'Triple',
        'd':'Doble',
        'i':'Individual'
        }
    print('Opciones:')
    opt = input('\nTamaños: Triple ( t ) Doble ( d ) Individual ( i ): ').lower()

    while opt not in list(sizes.keys()):
        print('=> ¡¡Debe seleccionar un tamaño correcto!!')
        opt = input('Tamaños: Triple ( t ) Doble ( d ) Individual ( i ): ').lower()

    return sizes[opt]
