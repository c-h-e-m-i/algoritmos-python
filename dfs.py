fh = open('input.txt', 'r')  # Abrimos el archivo con la entrada y guardamos los datos en una variable global

def crearGrafo(n, m):
    grafo = [[] for _ in range(n+1)]  # Nuestro grafo será un array de (n+1) listas de adyacencia
                                      # (añadimos el +1 porque empezamos a numerar los nodos desde el 1)
    for _ in range(m):  # Por cada arista que tengamos...
        u, v = [int(x) for x in next(fh).split()]  # ... leemos de dónde a dónde va
        grafo[u].append(v)  # Como en este caso son bidireccionales...
        grafo[v].append(u)  # ... añadimos el arista a las listas de ambos lados

    return grafo

def dfs(grafo, ini, fin, pasos, visitado):
    if ini == fin:  # Si el nodo en el que estamos es nuestro destino, devolvemos el número de pasos
        return pasos
    
    visitado[ini] = True  # Si no, lo marcamos como visitado...

    for vecino in grafo[ini]:  # ... y analizamos sus nodos vecinos
        if not visitado[vecino]:  # Si el vecino que estamos analizando no se ha visitado aún, nos movemos a él
            res = dfs(grafo, vecino, fin, pasos + 1, visitado)
            if res >= 0:  # Si dicho vecino nos devuelve un valor >= 0, significa que por su rama se ha llegado al destino
                return res  # Devolvemos, pues, el número de pasos que han sido necesarios para alcanzar dicho destino

    return -1  # Si hemos analizado todos nuestros vecinos (o éramos una hoja) y ninguno ha llegado al destino, devolvemos -1

if __name__ == "__main__":
    n, m, ini, fin = [int(x) for x in next(fh).split()]  # Leemos n.º de nodos y aristas, nodo inicial, y nodo destino
    grafo = crearGrafo(n, m)  # Creamos el grafo
    visitado = [False] * (n+1)  # Creamos la lista de visitados
    print(dfs(grafo, ini, fin, 0, visitado))  # Ejecutamos DFS sobre el grafo
    fh.close()  # Cerramos el archivo