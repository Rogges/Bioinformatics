import itertools as it

list1=['C','B','T', 'G', 'F', 'X', 'N','I', 'Y', 'A', 'P', 'S']

#combos creates a generator containing the partial permutations of list1 of size n
combos=it.permutations(list1,n)

#prints out each n_tuple
for n_tuple in combos:
  print(''.join(n_tuple))
