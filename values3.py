import re
s="""hello world,hi,there;
"""
def processos(expressao):
    # Dividir a expressão em tokens
    tokens = re.split(r'[\,\s]+', expressao)

    
    for token in tokens:
        print (token)

    return 

def main():
    
    processo =processos(s)
    

print("\x1b[43;37m")
if __name__ == "__main__":
    main()

