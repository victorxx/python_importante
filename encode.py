palavras = "victor goes duarte saib,".split()

for palavra in palavras:
    if "," in palavra or "?" in palavra or "!" in palavra:
        print(palavra[:-1])
