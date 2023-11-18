def es_operador_asignacion(lexema):
    operadores_asignacion = ['=', '+=', '-=', '*=', '/=', '%=']
    return lexema in operadores_asignacion


def tipo_operador_asignacion(entrada):
    lexemas = []
    i = 0

    while i < len(entrada) - 1:
        if entrada[i:i+2] in ('+=', '-=', '*=', '/=', '%='):
            inicio = i
            lexema = entrada[i:i+2]
            lexemas.append(('OPERADOR_ASIGNACION', lexema, inicio, inicio+1))
            i += 2
        elif entrada[i] == '=':
            inicio = i
            lexema = entrada[i]
            lexemas.append(('OPERADOR_ASIGNACION', lexema, inicio, inicio))
            i += 1
        else:
            i += 1

    if not lexemas:
        return 'DESCONOCIDO', entrada, 0, len(entrada) - 1
    else:
        return lexemas


# Ejemplo de uso
cadena = "a = 5 += b -= 3"
resultados = tipo_operador_asignacion(cadena)

for tipo, lexema, inicio, fin in resultados:
    print(f"Lexema: {lexema}, Tipo: {tipo}, Posición: {inicio}-{fin}")
