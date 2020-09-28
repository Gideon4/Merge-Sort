import random,time

def split(listo):
    if len(listo)!=1:
        a=split(listo[0:(len(listo))//2])
        b=split(listo[len(listo)//2:])
        return(combine(a,b))
    else:
        return listo
        
def combine(a,b):
    templist=[]
    while a!=[] and b!=[]:
        if a[0]>b[0]:
            templist.append(b[0])
            b.pop(0)
        else:
            templist.append(a[0])
            a.pop(0)
    if a==[]:
        templist+=b
    else:
        templist+=a
    return templist

def generatelist(length,rangeo):
    return [random.randint(0,rangeo) for i in range(length)]

print(split(generatelist(4096,65536)))
