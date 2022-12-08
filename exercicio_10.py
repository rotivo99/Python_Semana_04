#!/usr/bin/env python3

import sys

numero_1 = int(sys.argv[1])
numero_2 = int(sys.argv[2]) + 1

while numero_1 < numero_2:
    print(numero_1)
    numero_1 += 1
print('Finalizado.')
