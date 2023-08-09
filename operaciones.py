def suma(a,b):
    try:
        r= a+b
    except TypeError:
        print("Error: el tipo de dato no es válido")
    else:
        return r

def resta(a,b):
    try:
        r= a-b
    except TypeError:
        print("Error: el tipo de dato no es válido")
    else:
        return r
def producto(a,b):
    try:
        r= a*b
    except TypeError:
        print("Error: el tipo de dato no es válido")
    else:
        return r

def division(a,b):
    try:
        r= a/b
    except TypeError:
        print("Error: el tipo de dato no es válido")
    except ZeroDivisionError:
        print("Error: no es posible dividir por cero")
    else:
        return r