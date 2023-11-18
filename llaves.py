def es_llave(caracter):
    return caracter in ['{', '}']


def tipo_llave(entrada):
    lexemas = []
    i = 0

    while i < len(entrada):
        if es_llave(entrada[i]):
            inicio = i
            lexema = entrada[i]
            lexemas.append(('LLAVE', lexema, inicio, inicio))
            i += 1
        else:
            i += 1

    if not lexemas:
        return 'DESCONOCIDO', entrada, 0, len(entrada) - 1
    else:
        return lexemas


# Ejemplo de uso
cadena = "{a + b} * {c - d}"
resultados = tipo_llave(cadena)

for tipo, lexema, inicio, fin in resultados:
    print(f"Lexema: {lexema}, Tipo: {tipo}, Posición: {inicio}-{fin}")
