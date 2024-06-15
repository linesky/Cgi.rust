global varswords
global varsvalue
varswords=[]
varsvalue=[]

def varsadds(s:str,v:int):
    global varswords
    global varsvalue
    ss=s.strip()
    ss=ss.upper()
    vv=varsindex(ss)
    varswords=varswords+[ss]
    varsvalue=varsvalue+[v]
def varsindex(s:str)->int:
    global varswords
    global varsvalue
    count=0
    ss=s.strip()
    ss=ss.upper()
    lc=len(varswords)
    for n in range(lc):
        if varswords[n]==ss:
            return n
      
    return -1
def varsfind(s:str):
    global varswords
    global varsvalue
    count=0
    ss=s.strip()
    ss=ss.upper()
    lc=len(varswords)
    for n in range(lc):
        if varswords[n]==ss:
            return varsvalue[n]
      
    return None
def setvarsvalue(s:str,v:int):
    global varswords
    global varsvalue
    ss=s.strip()
    ss=ss.upper()
    vv=varsindex(ss)
    if vv==-1:
        varsadds(ss,v)
    else:
        varsvalue[vv]=v
    
def varsfind(s:str)->int:
    global varswords
    global varsvalue
    count=0
    ss=s.strip()
    ss=ss.upper()
    lc=len(varswords)
    for n in range(lc):
        if varswords[n]==ss:
            return varsvalue[n]
      
    return None


def varslist():
    global varswords
    global varsvalue
    lc=len(varswords)
    for n in range(lc):
        print(varswords[n]+"="+str(varsvalue[n]))



print("\x1bc\x1b[43;37m")
setvarsvalue("vars1",1)
setvarsvalue("vars2",2)
setvarsvalue("vars3",3)
setvarsvalue("vars4",4)
setvarsvalue("vars1",2)
setvarsvalue("vars2",3)
setvarsvalue("vars3",4)
setvarsvalue("vars4",5)
varslist()
