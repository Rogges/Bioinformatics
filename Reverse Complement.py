def rcomplement(string):
    #A list comprehension can be used to call the complement base for each based in the reversed string, then this new list can be joined 
    #into an empty string
    
    return ''.join([{'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}[x] for x in string[::-1]])

    
