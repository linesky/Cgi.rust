import re
s='2024-10-05'
def processos(expressao):
    # Dividir a expressão em tokens
    regExp= r'[\\/\-\.]+'
    tokens = re.split(regExp,expressao)
    for n in tokens:
        print(n)
    

    return 

def main():
    
    processo =processos(s)
    

print("\x1b[43;37m")
if __name__ == "__main__":
    main()

