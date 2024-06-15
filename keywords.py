global keywords
global keyvalue
keywords=[]
keyvalue=[]

def keyadds(s:str,v:int):
    global keywords
    global keyvalue
    ss=s.strip()
    ss=ss.upper()
    vv=keyindex(ss)
    keywords=keywords+[ss]
    keyvalue=keyvalue+[v]
def keyindex(s:str)->int:
    global keywords
    global keyvalue
    count=0
    ss=s.strip()
    ss=ss.upper()
    lc=len(keywords)
    for n in range(lc):
        if keywords[n]==ss:
            return n
      
    return -1
def keyfind(s:str):
    global keywords
    global keyvalue
    count=0
    ss=s.strip()
    ss=ss.upper()
    lc=len(keywords)
    for n in range(lc):
        if keywords[n]==ss:
            return keyvalue[n]
      
    return None
def setkeyvalue(s:str,v:int):
    global keywords
    global keyvalue
    ss=s.strip()
    ss=ss.upper()
    vv=keyindex(ss)
    if vv==-1:
        keyadds(ss,v)
    else:
        keyvalue[vv]=v
    
def keyfind(s:str)->int:
    global keywords
    global keyvalue
    count=0
    ss=s.strip()
    ss=ss.upper()
    lc=len(keywords)
    for n in range(lc):
        if keywords[n]==ss:
            return keyvalue[n]
      
    return None


def keylist():
    global keywords
    global keyvalue
    lc=len(keywords)
    for n in range(lc):
        print(keywords[n]+"="+str(keyvalue[n]))



print("\x1bc\x1b[43;37m")
setkeyvalue("fuc1",1)
setkeyvalue("fuc2",2)
setkeyvalue("fuc3",3)
setkeyvalue("fuc4",4)
setkeyvalue("fuc1",2)
setkeyvalue("fuc2",3)
setkeyvalue("fuc3",4)
setkeyvalue("fuc4",5)
keylist()
