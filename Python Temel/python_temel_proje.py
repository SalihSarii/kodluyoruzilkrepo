# Soru 1 FLATTEN FUNCTİON

def isList(x,fl):
    for v in x:
        if type(v) is list:
            isList(v,fl)
        elif len(x)-1==x.index(v):
            fl.append(v)
            return
        else:
            fl.append(v)

inputVal =["Salo","Alo",12,False,['Kedi','köpek','at'],[[1,5,6],[8,9,12]]]
flattenList=[]
isList(inputVal,flattenList)

print(f"Verilenler=> {inputVal}")
print(f"Dönüstürülen=> {flattenList}")


#SORU 2
def revList(x,rl):
    
    for v in x:
        if type(v) is list:
            revList(v,rl)
        elif len(x)-1==x.index(v):
            x.reverse()
            return
    return x    

inputVal =[[1,5,6],[8,9,12]]
print(f"Verilenler=> {inputVal}")
veri=inputVal.copy()
veri.reverse()
reverseList=[]
reverseList=revList(veri,reverseList).copy()
print(f"Dönüstürülen=> {reverseList}")


