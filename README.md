# WayFinder

**Número da Lista**: 1<br>
**Conteúdo da Disciplina**: Grafos1<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 211006957  |  Sebastián Héctor Zuzunaga Rosado |
| xx/xxxxxx  |  xxxx xxxx xxxxx |

## Sobre 
Descreva os objetivos do seu projeto e como ele funciona. 
O objetivo deste projeto é utilizar o algoritmo breadth first search para encontrar o caminho mais curto entre diferentes cidades do Brasil.
- Neste caso, o gráfo é criado usando um diretório python onde os nós são armazenados com seus respectivos vizinhos, cada nó também é uma lista onde os vizinhos estão.
- Para a função de adiciona_nodo, que será usada para criar uma cidade, cria-se uma lista vazia no diretório, a chave desta lista será colocada pelo usuário.
- Para a função de remover_nodo, os vizinhos do nó que queremos remover serão pesquisados, então o nó será removido nas listas dos respectivos vizinhos, e o nó em si será finalmente removido.
- Para a função de verificar_nodo, o nó é procurado no diretório usam a sua chave, se o nó existe retorna 1 se não 0.
- Para a função de adiciona_aresta, usada para criar conexões, um nó A é adicionado à lista de vizinhos de outro nó B, depois o nó B é adicionado à lista de vizinhos do nó A, já que este é um gráfico não direcionado.
- Para a função BFS primeiro se criam 2 listas, uma para armazenar os nodos já visitados e outra que conterá os caminhos percorridos, logo se faz uma verificação, se o nó começo é igual ao final, antes de começar com o loop então já se esta no lugar de destino e retorna -1, logo se inicia um loop, enquanto encontram elementos na fila de caminhos se executa o codigo, se extrai o primeiro caminho da cauda e deste caminho se extrai o primeiro elemento, é adicionado à lista de visitantes e todos os seus vizinhos são adicionados a uma cópia da estrada e, em seguida, este caminho é adicionado à lista, uma vez que chegar ao nó alvo retorna o caminho que alcanço, do contrário não retorna nada.
- Para a função mostrar_nodo á imprimir um nó, seguido isto para cada vizinho desse nó os respectivos vizinhos do nó serão impressos, isto é feito para cada nó no diretório.

## Screenshots
![image](https://github.com/sebazac332/Projeto-1-PA/assets/98188828/2774dce6-1ca9-4167-8681-671054506125)
![image](https://github.com/sebazac332/Projeto-1-PA/assets/98188828/69573d6b-be7f-4bf0-826c-a9974bec8702)
![image](https://github.com/sebazac332/Projeto-1-PA/assets/98188828/5b14e5e4-4c68-4fd2-adad-33ebe291424e)
![image](https://github.com/sebazac332/Projeto-1-PA/assets/98188828/a37337ca-0975-4670-a252-ff333f36d3dd)


## Instalação 
**Linguagem**: Python<br>
- **Prerequisitos**:<br>
  Python<br>
  Windows PowerShell<br>
- **Instruções**:<br>
  Abrir o Windows PowerShell<br>
  Usar o comando cd para chegar à pasta que contém o arquivo .py<br>
  Escrever o nome do programa com a extensão . py; neste caso CidadesCaminho.py<br>

## Uso <br>
Uma vez executado o programa aparecerá um menu com várias opções de 1 a 6.<br>
- Se 1 for escrito, a opção de criação de uma cidade está selecionada, criando uma cidade vazia sem vizinhos, o nome da cidade será escrito pelo usuário, uma verificação será feita para garantir que a cidade ainda não está no grafo.
- Se você digitar 2 você está tentando fazer uma conexão, você escreve a cidade para conectar e, em seguida, para qual você deseja conectar, uma verificação será feita para garantir que as 2 cidades existem.
- Se você digitar 3 você deseja remover uma cidade, o nome deve ser colocado pelo usuário, verifica se existe no grafo.
- Se você escrever 4 você quer verificar o estado de todas as cidades e aqueles que estão conectados.
- Se se escreve 5 se quer encontrar o caminho mais curto entre 2 cidades, se faz uma verificação para assegurar que as 2 existam, se realiza o algoritmo BFS modificado, se há um caminho entre as 2 cidades se escreve este, caso contrário, uma mensagem será escrita dizendo que não existe caminho.
- Se você escrever 6, você fecha o programa.

## Outros 
Quaisquer outras informações sobre seu projeto podem ser descritas abaixo.




