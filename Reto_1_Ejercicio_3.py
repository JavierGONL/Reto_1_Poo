
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