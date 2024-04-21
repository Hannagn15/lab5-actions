def sumar(a,b):
    return a + b 


if __name__=="__main__":
    print(sumar(5,3))


def restar(a, b):
    return a - b

if __name__ == "__main__":
    print(restar(5, 3))


def multiplicar(a, b):
    return a * b

if __name__ == "__main__":
    print(multiplicar(5, 3))


def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    else:
        return a / b

if __name__ == "__main__":
    print(dividir(5, 3))


