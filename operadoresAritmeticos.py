def es_operador_aritmetico(caracter):
    operadores_aritmeticos = ['+', '-', '*', '/', '%']
    return caracter in operadores_aritmeticos


def tipo_operador_aritmetico(entrada):
    lexemas = []
    i = 0

    while i < len(entrada):
        if entrada[i] in ('+', '-', '*', '/', '%'):
            inicio = i
            lexema = entrada[i]
            lexemas.append(('OPERADOR_ARITMETICO', lexema, inicio, inicio))
            i += 1
        else:
            i += 1

    if not lexemas:
        return 'DESCONOCIDO', entrada, 0, len(entrada) - 1
    else:
        return lexemas


# Ejemplo de uso
cadena = "5 + 3 * 2 - 7 / 4"
resultados = tipo_operador_aritmetico(cadena)

for tipo, lexema, inicio, fin in resultados:
    print(f"Lexema: {lexema}, Tipo: {tipo}, Posición: {inicio}-{fin}")
