
def operaciones(entrada_1, entrada_2 , operacion):
    if operacion == "+":
        return entrada_1 + entrada_2
    elif operacion == "-":
        return entrada_1 - entrada_2
    elif operacion == "*":
        return entrada_1 * entrada_2
    elif operacion == "/":
        return entrada_1 / entrada_2
    else:
        return "no es una operacion basica"

if __name__ == "__main__":
    entrada_1 = float(input("ingrese el primer numero: "))
    entrada_2 = float(input("ingrese el segundo numero: "))
    operacion = input("ingrese la operacion que desea realizar(solo el simbolo +, -, *, /): ")
    resultado = operaciones(entrada_1, entrada_2, operacion)
    print(resultado)