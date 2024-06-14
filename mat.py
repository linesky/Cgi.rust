import re

def processos(expressao):
    # Dividir a expressão em tokens
    tokens = re.findall(r'[\d.\d]+|[\+\-\*/\(\)]', expressao)

    
    for token in tokens:
        print (token)

    return 

def main():
    expressao = input("express: ")
    processo =processos(expressao)
    

print("\x1b[43;37m")
if __name__ == "__main__":
    main()

