#Ao informar o n-esimo termo da sequencia, o programa deve imprimir todos os termos de
#Fibonacci até o n-esimo termo
# Autor: Diego Vale do Nascimento - 09/10/2022

print('Encontrar o n-ésimo termo da Sequência de Fibonacci')
print('='*51)
n = int(input("Qual termo deseja encontrar: "))
print('-'*51)
t1 = 0
t2 = 1
print('{} - {}' .format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' - {}' .format(t3), end='')
    t1 = t2
    t2 = t3
    cont +=1
print(' - Fim')
print('-'*51)
print("O n-ésimo termo é: ", t3)