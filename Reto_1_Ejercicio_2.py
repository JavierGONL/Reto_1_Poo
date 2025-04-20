
def palindromo(palabra):
    palabra_invertida = ""
    for i in range(len(palabra)-1, -1, -1):
        palabra_invertida += palabra[i]
    if palabra == palabra_invertida:
        return True, palabra_invertida
    else:
        return False, palabra_invertida

if __name__ == "__main__":
    palabra = input("ingrese la palabra para verificar si es palindromo: ")
    resultado, palabra_invertida = palindromo(palabra)
    if resultado:
        print(f"la palabra {palabra} es palindromo")
    else:
        print(f"la palabra {palabra} no es palindromo, su inversa es {palabra_invertida}")