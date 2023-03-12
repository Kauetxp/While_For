# 4 - Faça um programa que peça ao usuário para digitar o número de vezes que ele quer jogar uma moeda.
# O programa deve simular o lançamento de uma moeda e imprimir o resultado de cada lançamento
# (cara ou coroa).
# No final, o programa deve imprimir o número total de caras e o número total de coroas.
# se a biblioteca abaixo para números aleatórios:
# import random resultado = random.randint(0, 1)
import random

vezes = int(input("Quantas vezes você quer jogar a moeda? "))
cara = 0
coroa = 0
while vezes > 0:
    moeda = random.randint(0,1)
    if moeda == 0:
        print("Cara")
        cara +=1
    else:
        print("Coroa")
        coroa +=1
    vezes -= 1
print("Cara =",cara,"\nCoroa =",coroa)



