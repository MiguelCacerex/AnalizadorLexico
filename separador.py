def es_separador(caracter):
    return caracter == ','


def tipo_separador(entrada):
    lexemas = []
    i = 0

    while i < len(entrada):
        if es_separador(entrada[i]):
            inicio = i
            lexema = entrada[i]
            lexemas.append(('SEPARADOR', lexema, inicio, inicio))
            i += 1
        else:
            i += 1

    if not lexemas:
        return 'DESCONOCIDO', entrada, 0, len(entrada) - 1
    else:
        return lexemas


# Ejemplo de uso
cadena = "a, b, c = 1, 2, 3"
resultados = tipo_separador(cadena)

for tipo, lexema, inicio, fin in resultados:
    print(f"Lexema: {lexema}, Tipo: {tipo}, Posición: {inicio}-{fin}")
