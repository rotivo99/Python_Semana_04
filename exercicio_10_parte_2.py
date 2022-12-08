#!/usr/bin/env python3

import sys

numero_1 = int(sys.argv[1])
numero_2 = int(sys.argv[2]) + 1

if numero_1 > numero_2:
    print('O primeiro número precisa ser menor do que o segundo.')
    sys.exit()
else:
    print('Números corretos. Prosseguindo.')

while numero_1 < numero_2:
    if numero_1 % 2 != 0:
        print(numero_1)
        numero_1 += 2
    else:
        numero_1 += 1

