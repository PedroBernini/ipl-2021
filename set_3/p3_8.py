# Programa para compor funcões.

def composite_result(f, g, x):
    return f(g(x))

def composite(f, g):
    return lambda x: f(g(x))