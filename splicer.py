def splicer(string,n):
    while n>0:
        intron=str(input('enter the intron'))
        string=string.replace(intron,'')
        n-=1
    return(string)
