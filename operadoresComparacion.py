def es_operador_comparacion(lexema):
    operadores_comparacion = ['==', '!=', '<=', '>=', '<', '>']
    return lexema in operadores_comparacion


def tipo_operador_comparacion(entrada):
    lexemas = []
    i = 0

    while i < len(entrada) - 1:
        if entrada[i:i+2] in ('==', '!=', '<=', '>='):
            inicio = i
            lexema = entrada[i:i+2]
            lexemas.append(('OPERADOR_COMPARACION', lexema, inicio, inicio+1))
            i += 2
        elif entrada[i] in ('<', '>'):
            inicio = i
            lexema = entrada[i]
            lexemas.append(('OPERADOR_COMPARACION', lexema, inicio, inicio))
            i += 1
        else:
            i += 1

    if not lexemas:
        return 'DESCONOCIDO', entrada, 0, len(entrada) - 1
    else:
        return lexemas


# Ejemplo de uso
cadena = "5 == 3 < 7 != 2 >= 8"
resultados = tipo_operador_comparacion(cadena)

for tipo, lexema, inicio, fin in resultados:
    print(f"Lexema: {lexema}, Tipo: {tipo}, Posición: {inicio}-{fin}")
