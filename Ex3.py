# 3 - Faça um programa que peça ao usuário para digitar uma sequência de números inteiros. 
# O programa deve imprimir a soma dos números digitados, mas parar a soma se o usuário
# digitar um número negativo.

print("Vou somar todos os numeros que você digitar. Quando quiser parar digite qualquer número negativo")

ct = 1
print("Digite o",ct,"º número: ")
n = int(input(""))
n2= 0
while n2>=0:
    ct+=1
    print("Digite o",ct,"º número: ")
    n2 = int(input(""))
    if n2 < 0:
        break
    else:
        n += n2
print(n)
