import operator

# Função para impressão dos itens (Essa função não é utilizada no momendo devido ao alto número de informações)
def imprime_itens():
    for i in range(len(solucao)):
        print('=' * 30)
        print(f'''
        Nome: {dados[i][0]}
        Peso: {dados[i][1]}
        Benefício: {dados[i][2]}''')

# Função que exibe a solução do algoritmo
def imprime_solucao():
    print('-----------------------------------------------------------')
    print(f'A mochila possui {peso} espaços e está ocupando {peso_atual} espaços.')
    print(f'\nO benefico da mochila é de {beneficio_atual}')
    print('-----------------------------------------------------------')
    print(f'Esses foram os itens levados:')
    for i in range(len(solucao)):  # Percorre o vetor solução para identificar qual item foi levado
        if solucao[i] == 1:  # Se o valor de i for igual a 1 o item foi levado
            print(f'''
Nome: {dados[i][0]}
Peso: {dados[i][1]}
Benefício: {dados[i][2]}''')

# Maximizar o benefício da solução final (levar itens com mais benefício)
def maximizar_beneficio():
    dados.sort(key=operator.itemgetter(2), reverse=True)  # Ordena beneficio decrescente
    print('\nA medida de desempenho utilizada foi a de maximizar o benefício da solução final')

# Utilizar uma medida de custo-benefício: beneficio/peso
def custo_beneficio():
    dados.sort(key=operator.itemgetter(2), reverse=True)  # Ordena beneficio decrescente
    dados.sort(key=operator.itemgetter(1))  # Ordena peso crescente
    print('\nA medida de desempenho utilizada foi a de custo/beneficio')

# Adicionar conteudo do arquivo .txt em um vetor
with open('instancias-mochila\KNAPDATA100000.txt', 'r') as arquivo:
    arquivos = arquivo.readlines()

# Declaração de variaveis e vetores
peso = int(arquivos[0])  # Peso total da mochila
total_itens = int(arquivos[1])  # Numero total de itens
peso_atual = 0  # Peso atual da mochila
beneficio_atual = 0 # Beneficio atual da mochila
fim = 0  # Sai do loop
opc = 0 # Entrada do usuário
dados = []  # Cria a lista de dados separados
solucao = []  # Cria uma lista informando se o item será levado ou não / 0 ou 1

del (arquivos[0])  # Deleta arquivos na posição 0 (Peso total da mochila)
del (arquivos[0])  # Deleta arquivos na posição 0 (Numero total de itens)

# Separação dos itens do arquivo
# Realização da conversão dos valores em inteiro
# Preenchimento do vetor solução com valor 0
for i, n in enumerate(arquivos):
    dados.append(n.split(',', 3))  # Separa os valores de cada item em três colunas (Nome, Peso, Benefício)
    dados[i][1] = int(dados[i][1])  # Converte valor do peso em int
    dados[i][2] = int(dados[i][2])  # Converte valor do beneficio em int
    solucao.append(0)  # Preenche a lista de solução com o valor inicial 0

# Entrada do usuário para definir a medida de desempenho
print('PROBLEMA DA MOCHILA (Algoritmo Guloso)')
print('1 - Maximizar o benefício da solução final (levar itens com mais benefício)')
print('2 - Utilizar uma medida de custo-benefício: beneficio/peso')
while opc != 1 or opc != 2:
    opc = int(input('Informe a opção desejada: '))
    if opc == 1:
        maximizar_beneficio() # Invoca a função de maximizar beneficio
        break
    elif opc == 2:
        custo_beneficio() # Invoca a função de custo/beneficio
        break
    else:
        print('Opção incorreta, tente novamente')

# Algoritmo guloso
while fim == 0:  # loop
    for i in range(len(solucao)):
        if (peso_atual + dados[i][1]) > peso:  # Se a mochila for preenchida encerra o loop
            fim = 1
        else:
            peso_atual += dados[i][1]  # Conta o peso atual da mochila em cada laço de repetição
            beneficio_atual += dados[i][2] # Conta o beneficio atual da mochila em cada laço de repetição
            solucao[i] = 1  # Vetor solução recebe 1 para indicar que o item foi levado

imprime_solucao()  # Imprime a solução do algoritmo