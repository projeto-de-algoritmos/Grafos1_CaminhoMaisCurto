# Crear lista de adjacencia
# Lista usa texto en lugar de numeros
# Creado BFS, falta verificar

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
        cola = [inicio]

        while cola:
            nodo_actual = cola.pop(0)
            if nodo_actual not in visitados and nodo_actual is not final:
                print(nodo_actual, end=' ')
                visitados.add(nodo_actual)
                cola.extend(vecino for vecino in self.grafo[nodo_actual])

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

print("Recorrido BFS a partir del nodo 'Brasilia':")
g.bfs("Gamma","Aguas claras")
