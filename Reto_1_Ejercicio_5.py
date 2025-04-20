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
                   
         