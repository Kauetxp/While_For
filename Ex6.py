print("Simulação de investimento na poupança por 12 meses")
p = int(input("Qual é o valor que você deseja investir? "))

n = 12
i = 0.5
m = (p * (1+i))**n
print("O investimento terá um retorno de: \nR$",round(m,2))
