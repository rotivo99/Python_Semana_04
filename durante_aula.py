#!/usr/bin/env python3

print(list(range(0,7)))
print(list(range(0,8))) #Você cria uma lista com os valores nesse intervalo

seq = 'ATTCTGCATGTCAGCATG'
print(list(range(0, len(seq))))

print('')

for inx in list(range(0, len(seq))):
    print(inx)

print('')

for inx in list(range(0, len(seq))):
    print(seq[inx])

print('')

c = 0
while c < 5:
    print(c)
    c += 1
print('Finalizado.')

