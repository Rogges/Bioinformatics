def hammettlength(t,v):
    ct=0
    for i in range(len(t)):
        if t[i]!=v[i]:
            ct+=1
    print(ct)
hammettlength('CAATACCAGCACTCACGATAACTCACGATTTCCCCTGAACAGCAGAGGTGATAATCTGTCCGCCTCATTGGCGCGTTGTGCCATGAGCGGTAAGTCCAGCGATCGGCAAGTCGTGTATTCGTCTTGGCCACATCGCATCGTTCCCTAGGTTTCAGGGGCATAGTCATTGATATCCGTTCGCACTGTCTGGTTTAGGACCGGTGTTACTGAGTGGATATCGCTTCACAATTCAATTGACATCAACCTATCACTTTGTTGGTAACGCTCTTGAATCCGGGCCCGGCGCGTTGATTGAATTCCTATCGATATTAGTCCTGAGCAGACGTGGGCTAGGGCAAGTAGCTCTTCCTAGGGGGTAACAATGGGCATCATGGTCGTTTCTGGAATCAGCTACAGGATGCAGGCAAGCTAAGCATTCGTTGTGAGATAACCATGCGAATCATGACCGTTTAATCGCCAGGATGACCGCTATGCATATCAACGGGTCCCTAACGGCAGCGGATAAAGAGCTAGTCTAGTTCATGGGTGAAACTTTAGGTCCATTATGTCAACTAGTATCGAGGTTTCCTATTAAGCGTACAAGTTAATGAGTTCTTCGGGCTGGCTCGCCGTAGATGTGACGGGTGTGCGCGGTCACAATCACGCAGGGCTTGCCGCATCTCCCACACACAGACGGGCGTCTTATACATCTTGCTTTGGTCGTAAAGCGATCCGGCTCATATTTTGGTTGTCACATCGTACTGGTCAGCATTTGAGTAGGATTGGAGGTTAATCCACGTGCTCTAGACTTCCATACATAGTTTTATCAACAGGAATTACCGAGAGGCATTAACTGATCCGAACACACACCGAGCAGCCTGTACCCATCATGCATCGAACCCTTTTCTCAACCAAAAGCCCCGTCTTAGCGACCAGAGGGGGCGTTCAACGCTGATTTATCCTCTGTCGTGGTTGTCAGTGAAAACAGGCCATATCTAATCGCGACGGCGCCTGCCC','CCAGACAAGTATAGCCGATAGATGGTGATTCCCGCTACGCAGCAAGGCTTATAGGATGTTTGTCTCATCCGGACCATTTGTGAAGCCCGGGCTGTCCGTCCTCCGACAATTGGTGTGTTTGGCTACGCCACGTCCCTCCTTTAAGTCCTTATCAGCGTGGCAACGGTATAGATCTGTGTGGCGTGTCTGTGTTGGGGGGTAGTGCTCGTGGGACAGTTACCAACCCAATTAAATTGCCAAATTTCCTGCACTTTGCGTGTTTCGGCCCTATCCTTCGGCCAGATGTGCACTTTGTTGTCATATGGATATTCTTAATGTGAAATCGAGTGTTTTTGGCAGTTACTCTGTCTACGGGGTAACAACGAACATGATGTACGGCTAAAAGAATACTCTGAAGTTCCCTAGATGTTTAGCACCCTGTTTAAGCTATGCTGCCATTCCATCATCTCTTGATCGGCTGGATGAATGATATCTGGCTAAATGGACCTTTCACGGCAACGCTTGGACTACTCCTTTAGTCTAGGGCTGTAACGTTAAGTCCGTTATGTCAACAAGCAACGCTCCTCCCGAGAAAGCTTACTGGTTAAAGAGTGCGTCCGGCATGCTCAAGCTAGGCTTTCCGGTCGGTCAGGAAACCTCTAGCGGAACGACGTCCCCTTGATCTATCGATTTGTCTCAGAAACGATAATCAGTCGCTCGGCGAGCGTCGGCGTGTTCTATCATATGAGTAACAGAGCGAACCTGGCTGCATACGACGAGGTCGATAGGGGAGTAAACGGAGGATCTTCTTAGCTACTTTGATTATAGAATTGGAAGAACACCGCGGTGTCTTATGAACATAACACCAGTCCACCAGCCATTACGGATCCTGCCTGTATTCACTTTCTGAACAGCAAGGCAGCCCTTCGAAACTCTAAAGTCTGGGGAGTGCATCGTTAACCAGCGCCTTCGGCTTAGGTAAGGGCAGGCCATATTAATTTTGCGCCCCGCCTGTCC')
    