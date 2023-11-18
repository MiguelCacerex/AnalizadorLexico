def es_parentesis(caracter):
    return caracter in ['(', ')']


def tipo_parentesis(entrada):
    lexemas = []
    i = 0

    while i < len(entrada):
        if es_parentesis(entrada[i]):
            inicio = i
            lexema = entrada[i]
            lexemas.append(('PARENTESIS', lexema, inicio, inicio))
            i += 1
        else:
            i += 1

    if not lexemas:
        return 'DESCONOCIDO', entrada, 0, len(entrada) - 1
    else:
        return lexemas


# Ejemplo de uso
cadena = "(5 + 3) * (2 - 1)"
resultados = tipo_parentesis(cadena)

for tipo, lexema, inicio, fin in resultados:
    print(f"Lexema: {lexema}, Tipo: {tipo}, Posición: {inicio}-{fin}")
