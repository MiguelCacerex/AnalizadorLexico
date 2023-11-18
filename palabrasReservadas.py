def es_palabra_reservada(lexema):
    palabras_reservadas = ['Bulbasaur', 'Ivysaur', 'Venusaur', 'Charmander',
                           'Charmeleon', 'Charizard', 'Squirtle', 'Wartortle', 'Blastoise']
    return lexema in palabras_reservadas


def tipo_palabra_reservada(entrada):
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

            if es_palabra_reservada(lexema):
                lexemas.append(('PALABRA_RESERVADA', lexema, inicio, fin - 1))
        else:
            i += 1

    if not lexemas:
        return 'DESCONOCIDO', entrada, 0, len(entrada) - 1
    else:
        return lexemas


# Ejemplo de uso
cadena = "Charmander Bulbasaur Pikachu Ivysaur Charmeleon"
resultados = tipo_palabra_reservada(cadena)

for tipo, lexema, inicio, fin in resultados:
    print(f"Lexema: {lexema}, Tipo: {tipo}, Posición: {inicio}-{fin}")
