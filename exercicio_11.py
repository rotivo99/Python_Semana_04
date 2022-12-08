#!/usr/bin/env python3

lista = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

for seq in lista:
    print(seq)

print('')

compreensao_lista = [print(seq) for seq in lista]

print('')

for seq in lista:
    print(len(seq),"\t"+seq)

print('')

compreensao_lista_2 = [print(len(seq),'\t'+seq) for seq in lista]

print('')

for index, seq in enumerate(lista):
    print(index + 1,'\t',len(seq),'\t'+seq, sep='')

print('')

compreensao_lista_3 = [print(index + 1,'\t',len(seq),'\t'+seq, sep='') for index, seq in enumerate(lista)]
