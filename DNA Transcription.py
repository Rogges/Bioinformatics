def transcribe(bases):
    return ''.join([x if x!="T" else "U" for x in bases])

