import re
s="""hello 10,10
world 20,20
hi 30,30;there 40,40
"""
def processos(expressao):
    # Dividir a expressão em tokens
    tokens = re.split(r'[;\n]+', expressao)

    
    for token in tokens:
        print("-----------line")
        print(token)
        varss = re.split(r'[,\s]', token)
        for vvar in varss:
            print ("    "+vvar)

    return 

def main():
    
    processo =processos(s)
    

print("\x1b[43;37m")
if __name__ == "__main__":
    main()

