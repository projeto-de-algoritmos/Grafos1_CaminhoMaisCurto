class Grafo:

    def __init__(self):
        self.grafo = {}

    def adiciona_nodo(self, nodo):
        if nodo not in self.grafo:
            self.grafo[nodo] = []

    def adiciona_aresta(self, u, v):
        self.grafo[u].append(v)
        self.grafo[v].append(u)


    def bfs(self, inicio, final):
        visitados = set()
        cola = [[inicio]]  

        if inicio == final:
            return -1

        while cola:
            camino = cola.pop(0)
            nodo_actual = camino[-1]

            if nodo_actual not in visitados:
                if nodo_actual == final:
                    return camino
                else:
                    visitados.add(nodo_actual)
                    for vecino in self.grafo[nodo_actual]:
                        nuevo_camino = list(camino)
                        nuevo_camino.append(vecino)
                        cola.append(nuevo_camino)

    def mostra_lista(self):
        for nodo, vecinos in self.grafo.items():
            print(f'{nodo}:', end ='  ')
            for vecino in vecinos:
                print(f'{vecino}  ->', end='  ')
            print('')


g = Grafo()

g.adiciona_nodo("Brasilia")
g.adiciona_nodo("Gamma")
g.adiciona_nodo("Floreanopolis")
g.adiciona_nodo("Aguas claras")

g.adiciona_aresta("Brasilia", "Gamma")
g.adiciona_aresta("Brasilia", "Floreanopolis")
g.adiciona_aresta("Floreanopolis", "Aguas claras")
g.adiciona_aresta("Aguas claras", "Brasilia")

g.mostra_lista()

camino_mas_corto = g.bfs("Gamma","Aguas claras")

if camino_mas_corto and camino_mas_corto != -1:
    print(f'El camino más corto es: {camino_mas_corto}')
elif camino_mas_corto == -1:
    print(f'Ya estas aqui')
else:
    print('No hay camino entre los nodos.')
