class Grafo:

    def __init__(self):
        self.grafo = {}

    def adiciona_nodo(self, nodo):
        if nodo not in self.grafo:
            self.grafo[nodo] = []

    def deletar_nodo(self, nodo):
        for vecino in self.grafo[nodo]:
            self.grafo[vecino].remove(nodo)
        del self.grafo[nodo]

    def verificar_nodo(self,nodo):
        if nodo not in self.grafo:
            return 1
        else:
            return 0

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

while True:
    print('######Bemvindo a WayFinder#######')
    print('Selecione uma opção')
    print('1.- Inserir uma cidade')
    print('2.- Conectar uma cidade')
    print('3.- Apagar uma cidade')
    print('4.- Verificar o estado das cidades')
    print('5.- Encontrar caminho mais curto')
    print('6.- Sair')
    option = input()

    if option == '1':
        nodo = input('Digite o nome da cidade: ')
        compin = g.verificar_nodo(nodo)
        if compin == 1:
            g.adiciona_nodo(nodo)
        else:
            print('A cidade já está registrada')
    elif option == '2':
        nodo = input('Digite o nome da cidade para conectar: ')
        nodo_con = input('Digite o nome da cidade para fazer a conexão: ')
        comp1 = g.verificar_nodo(nodo)
        comp2 = g.verificar_nodo(nodo_con)
        if comp1 == 1 or comp2 == 1:
            print('Alguma das cidades não existem')
        else:
            g.adiciona_aresta(nodo,nodo_con)
    elif option == '3':
        nodod = input('Digite o nome da cidade para apagar: ')
        compdel = g.verificar_nodo(nodod)
        if compdel == 1:
            print('Cidade não existe')
        else:
            g.deletar_nodo(nodod)
            print('A cidade foi apagada')
    elif option == '4':
        g.mostra_lista()
    elif option == '5':
        inicio = input('Coloque o nome da cidade de partida: ')
        final = input('Coloque o nome da cidade de destino: ')
        compinit = g.verificar_nodo(inicio)
        compfinal = g.verificar_nodo(final)
        if compinit == 1 or compfinal == 1:
            print('Algumaa das cidades não existem')
        else:
            camino_mas_corto = g.bfs(inicio, final)
            if camino_mas_corto and camino_mas_corto != -1:
                print(f'O caminho mais curto é: {camino_mas_corto}')
            elif camino_mas_corto == -1:
                print(f'Você já está aqui')
            else:
                print('Não há caminho entre as cidades.')
    elif option == '6':
        break