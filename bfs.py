from collections import deque # Usamos deque porque sacar elementos no finales de listas tiene coste O(n)

fh = open('input.txt', 'r') # Abrimos el archivo con la entrada y guardamos los datos en una variable global

def crearGrafo(n, m):
    grafo = [[] for _ in range(n+1)] # Nuestro grafo será un array de (n+1) listas de adyacencia
                                     # (añadimos el +1 porque empezamos a numerar los nodos desde el 1)
    for _ in range(m): # Por cada arista que tengamos...
        u, v = [int(x) for x in next(fh).split()] # ...leemos de dónde a dónde va
        grafo[u].append(v) # Como en este caso son bidireccionales...
        grafo[v].append(u) # ...añadimos el arista a las listas de ambos lados

    return grafo # Una vez leídas todas las aristas, devolvemos el grafo

def bfs(grafo, ini, fin):
    cola = deque() # Creamos la cola
    visitado = [False] * len(grafo) # Creamos el array de visitados
    visitado[ini] = True # Marcamos el nodo inicial como visitado
    cola.append((ini, 0)) # Añadimos el nodo inicial a la cola para poder entrar al while

    while cola:
        nodo, pasos = cola.popleft() # Sacamos el primer nodo de la cola y los pasos para llegar hacia él

        if nodo == fin: # Si dicho nodo es nuestro destino, devolvemos el n.º de pasos para llegar hacia él
            return pasos

        for vecino in grafo[nodo]: # Si no, analizamos sus vecinos:
            if not visitado[vecino]: # Si el vecino que estamos analizando no está visitado...
                visitado[vecino] = True # ...lo marcamos como visitado...
                cola.append((vecino, pasos + 1)) # ...y lo añadimos a la cola,
                                                 # indicando que para llegar a él
                                                 # hemos dado 1 paso desde el nodo en el que estábamos
    
    return -1 # Si hemos salido de la cola sin llegar a nuestro destino, significa que no se puede llegar,
              # lo cual simbolizamos devolviendo un -1



if __name__ == "__main__":
    n, m, ini, fin = [int(x) for x in next(fh).split()] # Leemos n.º de nodos y aristas, nodo inicial, y nodo destino
    grafo = crearGrafo(n, m) # Creamos el grafo
    print(bfs(grafo, ini, fin)) # Ejecutamos BFS sobre el grafo
    fh.close() # Cerramos el archivo