def calcular_mcd(a,b):
    # Función para calcular el máximo común divisor 
    # (MCD) usando el algoritmo de Euclides
    while b:
        a, b = ( b, (a % b) )
    return a

# Función principal para resolver el problema de las jarras
def resolver_jarras(a, b, c):
    ops = 0 # Contador de operaciones
    cola = [] # Cola para BFS (búsqueda en anchura)

    # Caso base: si la cantidad objetivo es mayor que ambas jarras, es imposible
    if c > max(a, b):
        return -1
    
    # Caso base: si la cantidad objetivo es igual a la capacidad de alguna jarra, solo se necesita una operación
    elif c == a or c == b:
        return 1
    
    # Caso base: si c no es múltiplo 
    # del MCD de a y b, es imposible
    elif c % calcular_mcd(a, b) != 0:
        return -1
    
    else:
        # Inicializamos las variables para la BFS
        grande = max(a,b)   # Capacidad de la jarra grande
        peque = min(a,b)    # Capacidad de la jarra pequeña
        casos_visitados = set() # Conjunto para guardar los estados ya visitados
        casos_visitados.add((0,0)) # Estado inicial: ambas jarras vacías
        cola.append( (0,0,0) )     # Añadimos el estado inicial a la cola (grande, peque, operaciones)
        while cola:
            grande_aux, peque_aux, ops = cola.pop(0) # Sacamos el primer estado de la cola
            
            # Para verter de la jarra grande a la jarra pequeña
            if grande_aux != 0 and peque_aux != peque:
                # Primer caso: se llena primero la jarra pequeña
                if grande_aux >= ( peque - peque_aux ):
                    # Si el estado resultante no ha sido visitado
                    if ( grande_aux-(peque - peque_aux), peque ) not in casos_visitados:
                        # Si no hemos llegado a la cantidad objetivo
                        if ( grande_aux - (peque - peque_aux) != c ):
                            casos_visitados.add( (grande_aux - (peque - peque_aux), peque) )
                            cola.append( (grande_aux - (peque - peque_aux), peque, ops + 1) )
                        else:
                            # Si llegamos a la cantidad objetivo, sumamos una operación y terminamos
                            ops += 1
                            break
                else: # Segundo caso: se vacía la jarra grande antes de llenar la pequeña
                    if ( 0, peque_aux + grande_aux ) not in casos_visitados:
                        if ( peque_aux + grande_aux != c ):
                            casos_visitados.add( (0, peque_aux + grande_aux) )
                            cola.append( (0, peque_aux + grande_aux, ops + 1) )
                        else:
                            ops += 1
                            break
            
            # Para verter de la jarra pequeña a la jarra grande
            if peque_aux != 0 and grande_aux != grande:
                # Primer caso: se vacía la jarra pequeña antes de llenar la grande
                if ( peque_aux <= (grande - grande_aux) ):
                    if ( grande_aux + peque_aux, 0 ) not in casos_visitados:
                        if ( grande_aux + peque_aux != c ):
                            casos_visitados.add( (grande_aux + peque_aux, 0) )
                            cola.append( (grande_aux + peque_aux, 0, ops + 1) )
                        else:
                            ops += 1
                            break
                else: # Segundo caso: se llena primero la jarra grande
                    if ( grande, peque_aux - (grande - grande_aux) ) not in casos_visitados:
                        if ( peque_aux - (grande - grande_aux) != c ):
                            casos_visitados.add( (grande, peque_aux - (grande - grande_aux)) )
                            cola.append( (grande, peque_aux - (grande - grande_aux), ops + 1) )
                        else:
                            ops += 1
                            break
            
            # Vaciar la jarra grande
            if ( grande_aux > 0 ) and ( (0, peque_aux) not in casos_visitados ):
                casos_visitados.add( (0, peque_aux) )
                cola.append( (0, peque_aux, ops + 1) )
            
            # Vaciar la jarra pequeña
            if ( peque_aux > 0 ) and ( (grande_aux, 0) not in casos_visitados ):
                casos_visitados.add( (grande_aux, 0) )
                cola.append( (grande_aux, 0, ops + 1) )

            # Llenar la jarra grande
            if ( grande_aux == 0 ) and ( (grande, peque_aux) not in casos_visitados ):
                casos_visitados.add( (grande, peque_aux) )
                cola.append( (grande, peque_aux, ops + 1) )

            # Llenar la jarra pequeña
            if ( peque_aux == 0 ) and ( (grande_aux, peque) not in casos_visitados ):
                casos_visitados.add( (grande_aux, peque) )
                cola.append( (grande_aux, peque, ops + 1) )
        
        return ops


# Leemos el número de casos de prueba
for _ in range(int(input())):
    a = int(input())
    b = int(input())
    c = int(input())

    print(resolver_jarras(a, b, c))