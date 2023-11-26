

def prim_szam_kereso(szam):
    primek = []
    for szam1 in range(2,szam):
        na = 0
        for sz in range(1,szam1+1):
            if szam1 % sz == 0:
                na = na + 1
                
        if na == 2:
            primek.append(szam1)
            
    return primek

print(prim_szam_kereso(100))
            