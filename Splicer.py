def splicer(string,n):
    
    #n is the number of introns you want spliced out from the string
    
    while n>0:
        intron=str(input('enter the intron'))
        string=string.replace(intron,'')
        n-=1
    
    #loop removes introns from the string of bases for as many introns declared by n
    
    print(string)
