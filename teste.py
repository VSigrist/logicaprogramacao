# cria e imprime matriz
def cria_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz


def imprime_matriz(matriz):
    for i in range(len(matriz)):
        linha = matriz[i]
        for j in range(len(linha)):
            print(matriz[i][j], end=" ")
        print()


matriz = cria_matriz(5, 4)
imprime_matriz(matriz)

#le precos e imprime nota fiscal
with open('precos.txt') as arquivo:
    try:
        linhas = arquivo.readlines()
        precos = list(map(lambda x: float(x), linhas))
    except:
        print('deu ruim')
    arquivo.close()

with open('./nota_fiscal.txt', 'w') as nota_fiscal:
    conteudo = []
    for preco in precos:
        conteudo.append(f'tomate \t {preco}')
        conteudo.append('=================================')
        conteudo.append(f'total \t {sum(precos)}')
        nota_fiscal.write(str.join('\n', conteudo))
    nota_fiscal.close()
    
# notafiscal_2
    produtos = []
precos = []
with open('compras.txt', 'r') as compras:
    try:
        linhas = compras.readlines()
        for linha in linhas:
            (produto, preco) = linha.split(',')
            print(f'{produto} - {preco}')
            produtos.append(produto)
            precos.append(float(precos))
    except:
        print('deu ruim')
    compras.close()

with open('./nota_fiscal_plus.txt', 'w') as nota_fiscal:
    linhas_da_nota = []
    for i in range(len(precos)):
        linhas_da_nota.append(f'{produto[i]} \t {preco[i]}')
        linhas_da_nota.append('====================')
        linhas_da_nota.append(f'total \t {sum(precos)}')
        nota_fiscal.write(str.join('\n', linhas_da_nota))
    nota_fiscal.close()

#
