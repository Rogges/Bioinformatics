def hammingdistance(string,string2):
    ct=0
    
    #creates a tracking variable which will track the number of single point mutations
    
    for i in range(len(string)):
        if string[i]!=string2[i]:
            ct+=1
    
    #loop compares each individual character within each string of bases; if they are not the same, it is considered a single point mutation
    
    print(ct)
