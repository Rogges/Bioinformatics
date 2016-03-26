def rcomplement(string):
    bases=list(string)
    
    # turning the string into a list allows for list comprehension manipulations
    
    bases=bases[::-1]
    
    # using a -1 slice step means the bases results in the nucleotide bases being reverse ordered
    
    bases=['t' if base=='A' else base for base in bases]
    bases=['A' if base=='T' else base for base in bases]
    bases=['c' if base=='G' else base for base in bases]
    bases=['G' if base=='C' else base for base in bases]
    
    # each successive base is transformed to its complement base and alternating U.Case and L.Case letters are used so things aren't overwritten
    
    bstring=''.join(bases)
    print(bstring.upper())

    # this returns the list of bases back into the string of bases
