#01 - Dada a lista L = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
# a) tamanho da lista.
# b) maior valor da lista.
# c) menor valor da lista.
# d) soma de todos os elementos da lista.
# e) lista em ordem crescente.
# f) lista em ordem decrescente.

""" L = [5, 7, 2, 9, 4, 1, 3]



print('tamanho da lista',len(L))
print('maior valor da lista.',max(L))
print('menor valor da lista.', min(L))
print('soma de todos os elementos da lista', sum(L))

L.sort()
print('lista em ordem crescente.', L)

L.reverse()
print('lista em ordem decrescente.',L)
 """
#02 - Utilizando listas, faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

""" quest = []

print("Responda 1 para Sim e 0 para Não\n")

quest.append(int(input("Telefonou para a vítima?[1/0]: ")))
quest.append(int(input("Esteve no local do crime?[1/0]: ")))
quest.append(int(input("Mora perto da vítima?[1/0]: ")))
quest.append(int(input("Devia para a vítima?[1/0]: ")))
quest.append(int(input("Já trabalhou com a vítima?[1/0]: ")))


if sum(quest) == 2:
    print("Suspeito")
elif sum(quest) == 3 or sum(quest) == 4:
    print("Cumplice")
elif sum(quest) == 5:
    print("Assassino") 
else:
    print("Inocente")    """



# 1. Crie um código em Python que pede qual tabuada o usuário quer ver, em
# seguida imprima essa tabuada.

""" num = int(input("Qual tabuada deseja imprimir?: "))

for i in range(1,11):
    print(f'{num} x {i} = ',num*i) """

# 2. Elaborar um programa para imprimir os números de 1 (inclusive) até 10
# (inclusive) em ordem decrescente.

""" for i in range(1,11):
    print(i, end = ' ')

for C in range(10, 0, -1):
    print(C, end = ' ') """

# 3. Faça um programa que leia o estado civil de 15 pessoas (Solteiro / Casado) e
# mostre ao final a quantidade de pessoas de cada estado civil.

""" estado_civil = []
for i in range(1, 16):
    estado_civil.append(input('Qual seu estado civil?(Solteiro[s] / Casado[c]): \n'))
    
print('Solteiros = ',estado_civil.count('s'))
print('Casados = ',estado_civil.count('c')) """


# 4. Faça um algoritmo que imprima 10 vezes a frase: “Go Blue”.

""" for i in range(1,11):
    print('Go Blue', end = ' ')  """


# 5. Faça um programa que mostre os valores numéricos inteiros ímpares situados
# na faixa de 0 a 20.

""" for i in range(1, 21, 2):
   print(i, end = ' ')  """


# 6. O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar
# a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi
# contratado para desenvolver o programa que monta a tabela de preços de pães,
# de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o
# exemplo abaixo:









