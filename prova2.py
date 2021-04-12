#1
def media():
    nota1 = int(input("Insira a nota do aluno: "))
    nota2 = int(input("Insira a nota do aluno: "))
    nota3 = int(input("Insira a nota do aluno: "))

    nota_final = (nota1 + nota2 + nota3) / 3

    return (F"Média do aluno é {nota_final}")

print(media())

#2
N = int(input("Insira o tamanho da lista: "))
lista = []
def lista():
  i = 0
  while i < N:
    num = input()
    lista.append(num)
    i += 1
  return lista
lista()

#3
def globo():
  entrada = input("Insira 'a' para Globo, 'b' para SBT e 'z' ou 'Z' para finalizar o programa: ")
  while entrada != 'z':
    if entrada == 'Z':
      break

    elif entrada == 'a':
      print("Globo")

    elif entrada == 'b':
      print("SBT")

    else:
      print("Inválido")
    entrada = input()
globo()

#4
def media_2():
  i = 0
  lista = input("Insira as médias dos alunos: ")
  list = lista.split()
  media_inferior = []
  
  while i < len(list):
      
    if int(list[i]) < 7:
      media_inferior.append(list[i])
    i += 1
    
    if len(media_inferior) < 0.25 * len(list):
      return "Professor Coxa"
    
    else:
     return "Professor Padrão"
      
print(media_2())
