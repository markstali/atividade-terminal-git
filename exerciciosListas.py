#01 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha 
# separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

""" print('Digite 7 numeros: ')
pares = []
impares = []
numCrescent = []
for i in range(7):
   num = int(input('Digite un numero: '))
   numCrescent.append(num)
   if num % 2 == 0:
      pares.append(num)
   else:
      impares.append(num)
    
numCrescent.sort()
pares.sort()
impares.sort()      
print('Numeros pares: ',pares)    
print('Numeros impares: ',impares)  
print('Numeros ordem crescente:', numCrescent)
numCrescent.sort(reverse=True)
print('Numeros ordem decrescente:', numCrescent) """

#02 - Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. 
# No final, mostre a matriz na tela, com essa formatação:

# [  1  ][  2  ][  3  ]
# [  4  ][  5  ][  6  ]
# [  7  ][  8  ][  9  ] 

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for c in range(3):
   for l in range(3):
      print(matriz[c][l], end='')
   print()   
 
#03 - Aprimore o desafio anterior, mostrando no final:
   # A) A soma de todos os valores pares digitados.
   # B) A soma dos valores da terceira coluna. 
   # C) O maior valor da segunda linha.




#04 - Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
#  cadastrando tudo em uma lista composta.
