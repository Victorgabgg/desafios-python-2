print("--Grupo 10--")
print("Victor Gabriel Guimarães")
print("Lucas Rullo Takimoto")
print("Mateus José Felix Silverio")
print("Questão 3")
print("\n")

a = 0

n = int(input("Digite o N par e >= 6 e <= 32: "))
if (n % 2 != 0 or n < 6 or n > 32):
    while(n % 2 != 0 or n < 6 or n > 32):
        print("Número inválido! Tente novamente")
        n = int(input("Digite o N par e >= 6 e <= 32: "))

a = (n//2)
aux = 2
p = a

print('\n')
#Cima
print(' '*a + '**  ')
print(' '*(a-1) + '****')

p-=2
for i in range(2,a):
    print(' '*p + '**' + ' '*aux + '**')
    aux+= 2
    p-=1

aux-=4
p+=2
for i in range(2,a-1):
    print(' '*p + '**' + ' '*aux + '**')
    aux-= 2
    p+=1

#Baixo
print(' '*(a-1) + '****')
print(' '*a + '**  ')


print('\n\nFim do programa.')



