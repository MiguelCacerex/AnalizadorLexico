def tipo_identificador(entrada):
    lexemas = []
    i = 0

    while i < len(entrada):
        if entrada[i].isalpha() or entrada[i] == '_':
            inicio = i
            es_valido = True
            contador = 0

            while i < len(entrada) and (entrada[i].isalnum() or entrada[i] == '_') and contador < 10:
                i += 1
                contador += 1

            fin = i

            lexema = entrada[inicio:fin]

            if contador > 0 and es_valido:
                lexemas.append(('IDENTIFICADOR', lexema, inicio, fin - 1))
        else:
            i += 1

    if not lexemas:
        return 'DESCONOCIDO', entrada, 0, len(entrada) - 1
    else:
        return lexemas


# Ejemplo de uso
cadena = "abc _variable123 invalid_id _another_long_id_here_12345"
resultados = tipo_identificador(cadena)

for tipo, lexema, inicio, fin in resultados:
    print(f"Lexema: {lexema}, Tipo: {tipo}, Posición: {inicio}-{fin}")
