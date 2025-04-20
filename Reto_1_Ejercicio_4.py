
def suma_mayor_dos_nuemeros_consecutivos():
    lista = []
    suma_mayor = 0
    while True: # bucle para ingresar los números
        numero = input("Digite um número (solo numeros, 0 para salir): ")
        if numero == "" or numero == " ":
            print("Digite um número válido") # casos de error basicos
        else:
            numero = int(numero)
        if numero == 0: # condición de salida
            break
        lista.append(numero)
    for i in range(len(lista)-1): # bucle para hallar la suma mayor
        if lista[i] + lista[i+1] > suma_mayor:
            suma_mayor = lista[i] + lista[i+1]
    return suma_mayor

if __name__ == "__main__":
    print(suma_mayor_dos_nuemeros_consecutivos())