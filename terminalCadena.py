def es_terminal(caracter):
    return caracter == ';'


def tipo_terminal(entrada):
    lexemas = []
    i = 0

    while i < len(entrada):
        if es_terminal(entrada[i]):
            inicio = i
            lexema = entrada[i]
            lexemas.append(('TERMINAL', lexema, inicio, inicio))
            i += 1
        else:
            i += 1

    if not lexemas:
        return 'DESCONOCIDO', entrada, 0, len(entrada) - 1
    else:
        return lexemas


# Ejemplo de uso
cadena = "if (a > b) { a = b; } else { a = c; }"
resultados = tipo_terminal(cadena)

for tipo, lexema, inicio, fin in resultados:
    print(f"Lexema: {lexema}, Tipo: {tipo}, Posición: {inicio}-{fin}")
