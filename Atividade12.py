#1
num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))

print(max(num1, num2, num3))

#2
a_file = open("aluno.txt", "r")

list_of_lists = []
for line in a_file:
    stripped_line = line.strip()
    line_list = stripped_line.split()
    list_of_lists.append(line_list)

a_file.close()

print(list_of_lists)

#3
lista = [3, 6, 3, 2, 1]

print(sum(lista))

#4
lista = ["seu", "joao", "esta", "aqui"]

lista_str = ' '.join(map(str, lista))
print(lista_str)
