#2 - Faça um programa que peça ao usuário para adivinhar um número entre 1 e 100.
# Enquanto o número digitado não for igual a um número secreto definido pelo programa
# o programa deve pedir ao usuário que tente novamente. Quando o usuário acertar o número,
# o programa deve imprimir "Parabéns, você acertou!".
# Use a biblioteca abaixo para números aleatórios: import random numero_secreto = random.randint(1, 100)

import random
numero_secreto = random.randint(1,100)

n = int(input("Advinhe o número secreto: "))

while n != numero_secreto:
    print("Você errou, tente novamente")
    n = int(input("Advinhe o número secreto: "))
print("Parabéns, você acertou")