
# Opción con enumerate (más eficiente que usar .index())
for i, dia in enumerate(lista):
        return dia

# Opción llamando al método .index(elemento)
for dia in diasSemana:
    if diasSemana.index(dia) == numeroSemana:
        return dia