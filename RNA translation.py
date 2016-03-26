def RNA2protein(bases):
    codontranslation={'UUU':'F','UUC':'F','UUA':'L','UUG':'L','UCU':'S','UCC':'S','UCA':'S','UCG':'S','UAU':'Y','UAC':'Y','UAA':'Stop','UAG':'Stop','UGU':'C','UGC':'C','UGA':'Stop','UGG':'W','CUU':'L','CUC':'L','CUA':'L','CUG':'L','CCU':'P','CCC':'P','CCA':'P','CCG':'P','CAU':'H','CAC':'H','CAA':'Q','CAG':'Q','CGU':'R','CGC':'R','CGA':'R','CGG':'R','AUU':'I','AUC':'I','AUA':'I','AUG':'M','ACU':'T','ACC':'T','ACA':'T','ACG':'T','AAU':'N','AAC':'N','AAA':'K','AAG':'K','AGU':'S','AGC':'S','AGA':'R','AGG':'R','GUU':'V','GUC':'V','GUA':'V','GUG':'V','GCU':'A','GCC':'A','GCA':'A','GCG':'A','GAU':'D','GAC':'D','GAA':'E','GAG':'E','GGU':'G','GGC':'G','GGA':'G','GGG':'G'}
    
    #the dictionary contains the corresponding amino acid for all 64 possible codons
    
    protein=''
    chunks,chunk_sz=len(bases),len(bases)//3
    chunk_sz=len(bases)//chunk_sz
    
    #chunk_sz creates groupings of length 3 that will later become the basis for codons
    
    codons=[ bases[i:i+chunk_sz] for i in range(0, chunks, chunk_sz) ]
    proteinlst=[]
    
    #codons stores the codons created by using chunk_sz; proteinlist stores the amino acids corresponding to each codon
    
    for codon in codons:
        aa=codontranslation[codon]
        if aa=='Stop':
            break
        elif True:
            proteinlst.append(aa)
    
    #for loop uses each codon to retrieve appropriate amino acid from the dictionary; if the amino acid is equivalent to 'Stop' the loop is broken because that is where translation would stop
    
    protein=protein.join(proteinlst)
    print(protein)
    
    #the list of amino acids are returned as a string representing the protein

