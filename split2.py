
ss="""
    func1 1,1,1,1
    func2 1,1,1,1;    func3 1,1,1,1; 
"""
def splitvalues(s:str)->list:
    a=[]
    s1=s.split(",")
    for nn in s1:
        s2=nn.split(" ")
        for n in s2:
            n=n.strip()
            if n!="":
                a=a+[n]
    return a
                    
def splits(s:str)->list:
    a=[]
    s1=s.split("\n")
    for nn in s1:
        s2=nn.split(";")
        for n in s2:
            n=n.strip()
            if n!="": 
                a=a+[n]    
    
    return a




print("\x1bc\x1b[43;37m")
s1=splits(ss)
for n in s1:
    print("--------line")
    print(">"+n)
    nn=splitvalues(n)
    for nnn in nn:
        print("    "+nnn)
