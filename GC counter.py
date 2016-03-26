def GC(bases,Fasta):
    CG=bases.count('G')+bases.count('C')
    percentGC=(CG/len(bases))*100
    
    #counts the amount of C and G bases in a given string and determines what percentage of the entire string it makes up
    
    print(Fasta)
    print(percentGC)
