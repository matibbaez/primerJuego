def color_random(lista_colores):
    from random import randrange
    return lista_colores[randrange(len(lista_colores))]

def color_aleatorio():
    from random import randint, randrange
    r = randrange(256)
    g = randrange(256)
    b = randrange(256)
    return (r, g, b)