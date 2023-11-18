def tipo_numero(entrada):
    lexemas = []
    i = 0

    while i < len(entrada):
        if entrada[i].isdigit() or entrada[i] == '.':
            inicio = i
            es_entero = True
            tiene_punto = False

            while i < len(entrada) and (entrada[i].isdigit() or entrada[i] == '.'):
                if entrada[i] == '.':
                    es_entero = False
                    tiene_punto = True
                i += 1

            fin = i

            lexema = entrada[inicio:fin]

            if tiene_punto:
                lexemas.append(('NUMERO_REAL', lexema, inicio, fin - 1))
            elif es_entero:
                lexemas.append(('NUMERO_ENTERO', lexema, inicio, fin - 1))
        else:
            i += 1

    if not lexemas:
        return 'DESCONOCIDO', entrada, 0, len(entrada) - 1
    else:
        return lexemas


# Ejemplo de uso
cadena = "123 3.14 45.67 789 abc"
resultados = tipo_numero(cadena)

for tipo, lexema, inicio, fin in resultados:
    print(f"Lexema: {lexema}, Tipo: {tipo}, Posición: {inicio}-{fin}")
