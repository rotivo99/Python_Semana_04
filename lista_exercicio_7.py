#!/usr/bin/env python3

#Somando o que é par e o que é ímpar na lista abaixo.
lista = [101,2,15,22,95,33,2,27,72,15,52]

soma_par = 0
soma_impar = 0

for n in lista:
    if n % 2 == 0:
        soma_par += n
    else:
        soma_impar += n

print(soma_par)
print(soma_impar)
