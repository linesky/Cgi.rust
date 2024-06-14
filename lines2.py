import re
s="""hello;
world;
hi;
there;
"""
def processos(expressao):
    # Dividir a expressão em tokens
    tokens = re.findall(r'([a-zA-Z1-9\.]+);', expressao)

    
    for token in tokens:
        print (token)

    return 

def main():
    
    processo =processos(s)
    

print("\x1b[43;37m")
if __name__ == "__main__":
    main()

