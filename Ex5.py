# 5 - Faça um programa que simule a urna eletrônica. A tela a ser apresentada deverá ser da seguinte forma:
# As opcoes sao:
#1. Candidato Jair Rodrigues
#2. Candidato Carlos Luz
#3. Candidato Neves Rocha
#4. Nulo
#5. Branco
#entre com o seu voto:
# O programa deverá ler os votos dos eleitores e, quando for entrado o número 6, apresentar as seguintes 
# informações: a) O número de votos de cada candidato; b) A porcentagem de votos nulos;
# c) A porcentagem de votos brancos; d) O candidato vencedor.
import time
print("As opções são: ")
print("1 - Candidato Jair Rodrigues\n2 - Candidato Carlos Luz\n3 - Candidato Neves Rocha")
print("4 - Voto nulo\n5Voto branco")
v = 0
JR = 0
CL = 0
NR = 0
NL = 0
BR = 0
while v < 6:
    v = int(input("Digite seu voto: "))
    if v == 1:
        JR +=1
    elif v ==2:
        CL +=1
    elif v ==3:
        NR +=1
    elif v ==4:
        NL+=1
    elif v ==5:
        BR+=1
print("Resultado:")
time.sleep(1)
print("Jair Rodrigues =",JR)
print("Carlos Luz =",CL)
print("Never Rocha =",NR)
time.sleep(1)
print((NL/100)*(JR+CL+NR+NL+BR),"%","de votos nulos")
print((BR/100)*(JR+CL+NR+NL+BR),"%","de votos brancos")
time.sleep(2)
if JR>CL and JR>NR:
    print("O vencedor foi: Jair Rodrigues")
elif CL>JR and CL>NR:
    print("O vencedor foi: Carlos Luz")
elif NR>JR and NR>CL:
    print("O vencedor foi: Neves Rocha")
else:
    print("Ouve um empate técnico")