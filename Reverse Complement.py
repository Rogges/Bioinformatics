def rcomplement(string):
    complement={'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    #A list comprehension can be used to call the complement base for each based in the reversed string, then this new list can be joined 
    #into an empty string
    
    return ''.join([complement[x] for x in string[::-1]])

    
def rcomplement2(string):
    return ''.join([{'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}[x] for x in string[::-1]])

#rcomplement is much faster than rcomplement2 but I figured it would be fun to have a one line solution to the problem
