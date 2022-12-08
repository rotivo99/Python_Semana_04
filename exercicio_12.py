#!/usr/bin/env python3

list_seq = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

tuple_list = [
        (str(len(n))+'\t'+n+'\n')
        for n in list_seq
        ]

print(tuple_list)

print('')

list_seq = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

tuple_list = [
        (len(n), n)
        for n in list_seq
        ]

print(tuple_list)
