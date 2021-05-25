# correcao da prova
# retornar maior entre 2

def maximo(n1, n2):
    if n1 > n2:
        return n1
    return n2

# media lista
def media(lista):
    soma = 0
    for elemento in lista:
        soma += elemento
    return soma/len(lista)

# media lista especifica
def exer3()
lista = [3, 7, 9, 0, 2, 11]
media_primeiros = media(lista[:3])
media_ultimos = media(lista[3:])
print(exer3(media_primeiros, media_ultimos))

# arquivos
notas = []
with open('./input.txt', 'r') as entrada:
    linhas = entrada.readlines()
    notas = list(map(lambda n: int(n), linhas))
    entrada.close()
with open('./saida.txt', 'r') as saida:
    conteudo.append(f'Minimo {min(notas)}')
    conteudo.append(f'Máximo {max(notas)}')
    conteudo.append(f'Média {sum(notas)/len(notas)}')
    saida.write(str.join('\n', conteudo))
    saida.close()

# matriz
def cria_matrix(nlinhas, ncolunas):
    from random import randint
    matrix =[]
    for i in range(nlinhas):
        linha = []
        for j in range(ncolunas):
            linha.append(randint(0,10))
        matrix.append(linha)
    return matrix
