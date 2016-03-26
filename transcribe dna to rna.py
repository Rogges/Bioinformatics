def transcribe(bases):
    bases=list(bases)
    bases1=['U' if base=='T' else base for base in bases]
    string=''.join(bases1)
    print(string)

