import random
print("--Grupo 10--")
print("Victor Gabriel Guimarães")
print("Lucas Rullo Takimoto")
print("Mateus José Felix Silverio")
print("Questão 2")
print("\n")
palpites = 0
num = 0
v = ""
r = ""
palpitesV = []

Min = int(input("Digite o valor de Min: "))
Max = int(input("\nDigite o valor de Max > Min+100: "))
if (Max <= (Min+100)):
    while(Max <= (Min+100)):
        Max = int(input("\nValor inválido o valor de Max deve ser > Min+100: "))

esc = int(input("\nDigite 1 para advinhar e 2 para sortear um num: "))
if (esc == 1):
    print("Você escolheu advinhar um número.")
    n = random.randint(Min,Max)

    while (num!= n):
            num = int(input("\nDigite o seu palpite: "))
            palpites+= 1
            palpitesV.append(num)
            
            if(num < n):
                print("O número sorteado é maior!")
            elif(num > n):
                print("O número sorteado é menor!")
            else:
                print("Você acertou!!!")
                print("A quantidade de palpites foi: {}".format(palpites))
                print("Os palpites foram {}".format(palpitesV))

elif(esc ==2):
    print("Você escolheu sortear um número.")
    num = int(input("\nDigite o número para o computador advinhar: "))

    while(v != "certo"):
        n = random.randint(Min,Max)
        palpites+= 1
        if (r):
            if(r == "maior"):
                while(n < lastN):
                    n = random.randint(Min,Max)
            else:
                while(n > lastN):
                    n = random.randint(Min,Max)
        lastN = n
        palpitesV.append(n)
        print("\nHmm pensando em um número...")
        print("O número é {}?".format(n))
        v = str(input("\nEstá (Certo) ou (Errado)?: ").lower().strip())
        if (v == "certo"):
            print("\nAcertei, então é o número {}!!".format(n))
            print("\nA quantidade de palpites foram {}".format(palpites))
            print("Os palpites foram {}".format(palpitesV))
        else:
            r = str(input("O número é (maior) ou (menor)?: ").lower().strip())

else:
    print("Escolha inválida.")
