#!/usr/bin/env python3

count = 0
while count < 15:
    print("Count:", count)
    count += 1
print('Finished the loop')

print('')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Entrada inválida.')

print('')
words = ['zero','one','two','three','four']
for word in words:
    print(word)

dna = 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'
for nt in dna:
      print(nt)
