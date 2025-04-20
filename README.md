## Reto 1

1. Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación. *entrada:* `(1,2,"+")`, *salida* `(3)`.

```python
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
```
##### Explicacion: simplemente se creo una funcion que toma 3 argumentos, 2 numeros y la operacion a realizar entre ellos, el bloque de ejecucion hay 2 inputs para los dos numeros y otro input en el cual se especifica la operacion
  
2. Realice una función que permita validar si una palabra es un palíndromo. **Condición:** No se vale hacer slicing para invertir la palabra y verificar que sea igual a la original.

```python

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
```
##### Explicacion: se usa una funcion que recorre la palabra de la ultima letra a la primera y va agregando a una lista, al final se compara si son la misma palabra y dependiendo de eso devuelve un True o False

3. Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.
```python
def devolver_primos(lista):
    primos = []
    for i in lista: 
        if i == 2 : # 2 es el unico numero primo par
            primos.append(i)
        else:
            # Si el numero es divisible por algun número distinto de 1 y de si mismo, no es primo
            for j in range(2, i): 
                if i % j == 0:
                    break
            else:
                primos.append(i)   

    for k in primos:
        if k == 1:
            primos.remove(k) # 1 no es primo
        for g in primos:
            if k % g == 0 and k != g: # Si el modulo de k por otro supuesto primo es 0, no es primo
                primos.remove(g)
    return primos

if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,12,13,26,17]
    resultado = print(devolver_primos(numeros)) # [2, 3, 5, 7, 11, 17]
```
##### Explicacion: la funcion agrega por defecto el 2 al ser el unico primo par a una lista y de resto calcula el modulo respecto a esa lista si es 0 no es primo, de resto es primo, por ultimo hace una verificacion de los numeros en la lista para corroborar que todos sean primos

4. Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.
```python
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

```
##### Explicacion: se agrega todos los numeros ingresados a una lista, luego en la funcion, recorre sumando numeros consecutivos la suma se compara con una variable suma_mayor y si es mayor se remplaza el valor en caso de que no sigue recorriendo la lista

5. Escribir una función que reciba una lista de string y retorne unicamente aquellos elementos que tengan los mismos caracteres. e.g. entrada: `["amor", "roma", "perro"]`, salida `["amor", "roma"]`
```python
def mismos_caracteres(lista_palabras):
    palabras_caracteres_iguales = []
    for i in range(len(lista_palabras)):
        # Comenzamos desde i + 1 para evitar comparaciones duplicadas
        for j in range(i + 1, len(lista_palabras)): 
            # sorted ordena los caracteres de la a a la z
            if sorted(lista_palabras[i]) == sorted(lista_palabras[j]):
                if lista_palabras[i] not in palabras_caracteres_iguales:
                    palabras_caracteres_iguales.append(lista_palabras[i])
                if lista_palabras[j] not in palabras_caracteres_iguales:
                    palabras_caracteres_iguales.append(lista_palabras[j])

    return palabras_caracteres_iguales

if __name__ == '__main__':
    lista_palabras = ['hola', 'arroz', 'zorra', 'pasos', 
                      'mundo', 'aloh', 'reconocer', 'reconocer',
                      'amor', 'roma', 'mora', 'moneda']
    print(mismos_caracteres(lista_palabras))
```
##### Explicacion: la funcion simplemente organiza los caracteres de una lista con sorted, que los ordena de A ala Z y luego de eso compara si las palabras son iguales en caso de ser, se agrega a la lista que retornamos
