import time

inicio = time.time()

MATRIZ_TESTE = []
MELHOR_CAMINHO = []
PONTOS_E_COORDENADAS = {}
MENOR_CUSTO = 0

def lerMatriz():

    global MATRIZ_TESTE, PONTOS_E_COORDENADAS
    with open("matriz", "r") as arquivo:

        matriz = arquivo.readlines()
        cont_linha = 0
        cont_coluna = 0

        for linha in matriz:
            MATRIZ_TESTE.append(linha.split())

    del MATRIZ_TESTE[0]

    for linha in MATRIZ_TESTE:
        cont_coluna = 0
        cont_linha += 1
        for elemento in linha:
            cont_coluna += 1
            if elemento != "0":
                PONTOS_E_COORDENADAS[elemento] = (cont_linha - 1, cont_coluna - 1)

    PONTOS_E_COORDENADAS.pop("R")

def calcularCusto(caminho, values):

    global MENOR_CUSTO, MELHOR_CAMINHO

    custo = 0
    custo_total = 0

    coordenadas = []

    for nome in caminho:
        coordenadas.append(values[nome])

    percorrer = [(3, 0)] + coordenadas + [(3, 0)]
    for i in range(len(percorrer) - 1):
        city_A = percorrer[i]
        city_B = percorrer[i + 1]
        custo += abs((city_A[0] - city_B[0])) + abs((city_A[1] - city_B[1]))
    custo_total = custo
    if MENOR_CUSTO == 0:
       MENOR_CUSTO = custo_total
    elif custo_total < MENOR_CUSTO:
        MENOR_CUSTO = custo_total
        MELHOR_CAMINHO = caminho
    return (MENOR_CUSTO, MELHOR_CAMINHO)

def criarPermutacoes(lista):

    conjunto = []
    for nomes in lista:
        conjunto.append(nomes)

    #Paso Base
    if len(conjunto) == 0:
        return []
    if len(conjunto) == 1:
        return [conjunto]

    lista_de_permutas = []#lista auxiliar que guardará todas permutações

    for index in range(len(conjunto)):
        chave = conjunto[index] #elemento que vai ser "travado"

        removedor = conjunto[:index] + conjunto[index + 1:]#lista sem o "chave"
        #cria uma lista auxiliar com o elemento travado + as permutações
        for p in criarPermutacoes(removedor):
            lista_de_permutas.append([chave] + p)

    return lista_de_permutas #retorna a lista de permutações

def calcularRota():
    lerMatriz()
    for permutacao in criarPermutacoes(PONTOS_E_COORDENADAS):
        calcularCusto(permutacao, PONTOS_E_COORDENADAS)
    print(f"A melhor rota {MELHOR_CAMINHO} tem o custo de {MENOR_CUSTO} dronômetros")


calcularRota()

fim = time.time() - inicio

print(f"Tempo de Execução: {time.time() - inicio}")




# --------------------------------------
