print("--Grupo 10--")
print("Victor Gabriel Guimarães")
print("Lucas Rullo Takimoto")
print("Mateus José Felix Silverio")
print("Questão 1")
print("\n")

i = 0
v = []
c = 0
aux = 0
somaprimos = 0
num = 0

Min = int(input("\nDigite o valor do Min > 1: "))
if (Min <= 1):
    while(Min <=1):
        Min = int(input("Numero invalido, digite o Min > 1: "))

Max = int(input("Digite o valor do Max > Min: "))
if (Max <= Min):
    while(Max <= Min):
        Max = int(input("Numero invalido, digite o Max > Min: "))


print("\nMin = {} e Max = {}".format(Min,Max))

for i in range(Min, Max+1):
    aux=0
    for c in range(1, Max+1):
        if(i % c == 0):
            aux+=1
    if(aux == 2):
        v.append(i)
        somaprimos+= i

if v:
    print("\nA quantidade de numeros primos é: ")
    for num in v:
        print(num)
    print("\nO total de numeros é {}.".format(len(v)))
    print("\nA soma dos primos é {}.".format(somaprimos))
else:
    print("Não há primos no intervalo [{}, {}].".format(Min,Max))


print("\n\nFim do Programa")
