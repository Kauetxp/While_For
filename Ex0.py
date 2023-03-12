#0 - Peça para  o usuário entrar com dois valores (primeiro e último).
# Faça a contagem entre esses números.
# Caso o último for menor que  o primeiro faça a contagem decrescente.
# Caso o último número for maior que o primeiro faça a contagem crescente.

n1=int(input("Digite um número:"))
n2=int(input("Digite um segundo número: "))
ct=5
ct2=0
if n2<n1:
    while ct >= 0:
        print(ct)
        ct-=1
else:
    while ct2 <=5:
        print(ct2)
        ct2+=1