def calcular_mcd(a, b):
    while b:
        a, b = (b, (a % b))
    return a

a = 7
b = 2
c = 4

if c > max(a, b):
    print(-1)
elif c == a or c == b:
    print(1)
else:
    grande = max(a, b)
    peque = min(a, b)
    casos_visitados = set()
    cola = []
    # Each state: (grande_aux, peque_aux, pasos)
    cola.append((0, 0, 0))
    casos_visitados.add((0, 0))
    found = False

    while cola:
        grande_aux, peque_aux, pasos = cola.pop(0)

        # Check if we reached the goal
        if grande_aux == c or peque_aux == c:
            print(pasos)
            found = True
            break

        # All possible next states
        siguientes = [
            (grande, peque_aux),               # Fill grande
            (grande_aux, peque),               # Fill peque
            (0, peque_aux),                    # Empty grande
            (grande_aux, 0),                   # Empty peque
            # Pour grande -> peque
            (grande_aux - min(grande_aux, peque - peque_aux), peque_aux + min(grande_aux, peque - peque_aux)),
            # Pour peque -> grande
            (grande_aux + min(peque_aux, grande - grande_aux), peque_aux - min(peque_aux, grande - grande_aux))
        ]

        for estado in siguientes:
            estado_simple = (estado[0], estado[1])
            if estado_simple not in casos_visitados:
                casos_visitados.add(estado_simple)
                cola.append((estado[0], estado[1], pasos + 1))

    if not found:
        print(-1)
