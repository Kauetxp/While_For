#1 - Ler um valor inteiro (aceitar somente valores entre 1 e 10) e
# escrever a tabuada de 1 a 10 do valor lido

n = int(input("Digite um número: "))
while n<1 or n>10:
    print("O número deve estar entre 1 e 10")
    n = int(input("Digite um número: "))
t = 1
while t<=10:
    print(n,"x",t,"=",n*t)
    t+=1
print("Pronto")
