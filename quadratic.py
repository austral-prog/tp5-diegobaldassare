# Replace the "ANSWER HERE" for your answer

def roots(a, b, c):
    """Dado los parámetros (a, b, c) el método roots devolverá un String de la forma “(r1, r2)” o “(r12)” o “( )”
    según sea el caso de que tenga dos raíces, una raíz o ninguna."""
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        r1 = (-b + discriminant**0.5) / (2*a)
        r2 = (-b - discriminant**0.5) / (2*a)
        return f"({r1}, {r2})"
    elif discriminant == 0:
        r = -b / (2*a)
        return f"({r})"
    else:
        return "( )"

def value_y(a, b, c, x):
    """Dado los parámetros (a, b, c, x) el método value_y devolverá el valor de Y para un valor de X que se le pasa como parámetro."""
    return a*x**2 + b*x + c


def to_string(a, b, c):
    """Dado los parámetros (a, b, c) el método to_string que devolverá un String mostrando la ecuación
    “f(x) = A * X^2 + B * X + C” reemplazando los valores de a, b y c.
    Si el coeficiente es 0 entonces no devolver el término de X"""
    terms = []
    if a != 0:
        terms.append(f"{a} * X^2")
    if b != 0:
        terms.append(f"{b} * X")
    if c != 0:
        terms.append(f"{c}")
    if not terms:
        return "f(x) = 0"
    return "f(x) = " + " + ".join(terms)

def derivation(a, b, c):
    """Dado los parámetros (a, b, c) el método derivation que devolverá un String mostrando la función lineal
    que resulta de derivar la función cuadrática. Si el coeficiente es 0 entonces no devolver el término de X"""
    if a == 0 and b == 0:
        return "f'(x) = 0"
    elif a == 0:
        return f"f'(x) = {b}"
    elif b == 0:
        return f"f'(x) = {2*a} * X"
    else:
        return f"f'(x) = {2*a} * X + {b}"