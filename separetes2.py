import re
s='func1(func2());'
def processos(expressao):
    # Dividir a expressão em tokens
    regExp= r'([A-za-z0-9*]+)\(\)'
    tokens = re.findall(regExp,expressao)

    
    for token in tokens:
        print (token)

    return 

def main():
    
    processo =processos(s)
    

print("\x1b[43;37m")
if __name__ == "__main__":
    main()

