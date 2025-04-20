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
        if i == 2 : # 2 es el unico número primo par
            primos.append(i)
        else:
            # Si el numero es divisible por algún número distinto de 1 y de sí mismo, no es primo
            for j in range(2, i): 
                if i % j == 0:
                    break
            else:
                primos.append(i)   
    return primos

if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    resultado = print(devolver_primos(numeros)) # [2, 3, 5, 7, 11]
```
##### Explicacion:
4. Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.
```python


```
##### Explicacion:
5. Escribir una función que reciba una lista de string y retorne unicamente aquellos elementos que tengan los mismos caracteres. e.g. entrada: `["amor", "roma", "perro"]`, salida `["amor", "roma"]`
```python
```
##### Explicacion:
