#!/usr/bin/env python3

lista = [234, 38, 3819, 4827, 928, 1829, 3912, 3849, 283, 2398]

soma_par = 0
soma_impar = 0

for n in lista:
    if n % 2 == 0:
        soma_par += n
    else:
        soma_impar += n

print(soma_par)
print(soma_impar)

print('')

soma_par_compreensao = 0
soma_impar_compreensao = 0

sum_of_evens = [soma_par_compreensao + n for n in lista if n % 2 == 0]
print(sum(sum_of_evens))
sum_of_odds = [soma_impar_compreensao + n for n in lista if n % 2 != 0]
print(sum(sum_of_odds))
