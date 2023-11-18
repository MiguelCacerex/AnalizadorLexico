def es_operador_incremento_decremento(lexema):
    operadores_incremento_decremento = ['++', '--']
    return lexema in operadores_incremento_decremento


def tipo_operador_incremento_decremento(entrada):
    lexemas = []
    i = 0

    while i < len(entrada) - 1:
        if entrada[i:i+2] in ('++', '--'):
            inicio = i
            lexema = entrada[i:i+2]
            lexemas.append(('OPERADOR_INC_DEC', lexema, inicio, inicio+1))
            i += 2
        else:
            i += 1

    if not lexemas:
        return 'DESCONOCIDO', entrada, 0, len(entrada) - 1
    else:
        return lexemas


# Ejemplo de uso
cadena = "a++ --b c++"
resultados = tipo_operador_incremento_decremento(cadena)

for tipo, lexema, inicio, fin in resultados:
    print(f"Lexema: {lexema}, Tipo: {tipo}, Posición: {inicio}-{fin}")
