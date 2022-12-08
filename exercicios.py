#!/usr/bin/env python3

taxa = 'erectus, sapiens, neanderthalensis'
print(taxa)
print(taxa[1])
print(type(taxa))

print('')

species = taxa.split(', ')
print(species)

print(species[1])
print(type(species))

print('')

print(sorted(species, reverse = False))
print(sorted(species, key = len))
