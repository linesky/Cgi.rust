import re
s='08:09:00:AM'
def processos(expressao):
    # Dividir a expressão em tokens
    regExp= r'([A-Za-z0-9*]+):*'
    tokens = re.findall(regExp,expressao)
    for n in tokens:
        print(n)
    

    return 

def main():
    
    processo =processos(s)
    

print("\x1b[43;37m")
if __name__ == "__main__":
    main()

