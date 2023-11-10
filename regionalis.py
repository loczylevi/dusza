"""
max sebesség személyautók és motorok számára 130 km/h,
autóbuszoknak 100 km/h
teherautóknak 80 km/h

"""

#Az adatcsomag első sorában 3 adat jelenik meg, ami a három mérőműszer helyét adja meg az út
#elejétől km-ben mért távolság alapján.

#a mérőhely kódja (A: az 1. műszer; B: a 2. műszer; C: a 3. műszer
#a jármű típusa (sz=személyautó; m= motor; b=autóbusz, t= teher;
#mk=megkülönböztetett)

class Autok:
    def __init__(self,sor):
        felseg_jel, rendszam, meres_helye, jarmu_tipus, sebesseg, meres_ideje = sor.strip().split(",")
        self.felseg_jel = felseg_jel
        self.rendszam = rendszam
        self.meres_helye = meres_helye
        self.jarmu_tipus = jarmu_tipus
        self.sebesseg = int(sebesseg)
        self.meres_ideje = meres_ideje
        #self.ora = int(meres_ideje[0:2])
        #self.perc = int(meres_ideje[3:5])
        #self.secundum = int(meres_ideje[6:8])
        
        
with open("D22.txt","r",encoding="UTF-8") as f:
    elso_sor = f.readline()
    lista = [Autok(sor) for sor in f]
    
    
    
#1. Az A mérési ponton hány motorkerékpár haladt el a megengedett sebességhatár felett?

hany_db = 0

for sor in lista:
    if sor.meres_helye == "A" and sor.jarmu_tipus == "m" and sor.sebesseg > 130:
        hany_db += 1
        
egysor = len([sor for sor in lista if sor.meres_helye == "A" and sor.jarmu_tipus == "m" and sor.sebesseg > 130])

print("1. feladat")

print(str(egysor) + "\n")

"""2. A B mérési ponton melyik rendszámú személyautók/buszok/teherautók mentek a megengedett sebesség felett és mennyivel?
Az érintett gépkocsik típusát, felségjelét, rendszámát és mellette a sebesség túllépés értékét
kell kiírni.
"""

def meghaladta_e(bemenet, meres_pont):
    szoveg = ""
    for sor in bemenet:
        if sor.meres_helye == meres_pont:
            if sor.sebesseg > 130 and sor.jarmu_tipus == "sz":
                szoveg = szoveg + f"{sor.jarmu_tipus} {sor.felseg_jel} {sor.rendszam} {sor.sebesseg-130}\n"
            if sor.sebesseg > 100 and sor.jarmu_tipus == "b":
                szoveg = szoveg + f"{sor.jarmu_tipus} {sor.felseg_jel} {sor.rendszam} {sor.sebesseg-100}\n"
            if sor.sebesseg > 80 and sor.jarmu_tipus == "t":
                szoveg = szoveg + f"{sor.jarmu_tipus} {sor.felseg_jel} {sor.rendszam} {sor.sebesseg-80}\n"
    return szoveg


print("2. feladat")

print(meghaladta_e(lista, "B"))

"""3. Mekkora volt a legnagyobb mért sebesség a C pontban az adott napon? Ezzel túllépte-e a
legnagyobb sebességgel haladó jármű a megengedett sebességet?
Jelenjen meg a mért legnagyobb sebesség, értelemszerűen a „túllépte”/”nem _lépte _túl”
szöveg, a jármű típusa, felségjele, rendszáma és a mérés ideje!
Ha több ilyen jármű is van, mindegyik adatait ki kell írni."""

legnagyobb = []

for sor in lista:
    if sor.meres_helye == "C":
        if sor.sebesseg > 130 and sor.jarmu_tipus == "sz" or sor.jarmu_tipus == "m":
            legnagyobb.append([sor.sebesseg, sor.jarmu_tipus, sor.felseg_jel, sor.rendszam, sor.meres_ideje])
        if sor.sebesseg > 100 and sor.jarmu_tipus == "b":
            legnagyobb.append([sor.sebesseg, sor.jarmu_tipus, sor.felseg_jel, sor.rendszam, sor.meres_ideje])
        if sor.sebesseg > 80 and sor.jarmu_tipus == "t":
            legnagyobb.append([sor.sebesseg, sor.jarmu_tipus, sor.felseg_jel, sor.rendszam, sor.meres_ideje])

        
nagy = 0
tipus = ""
felsegjele = ""
rendszama = ""
meres = ""
for sor in legnagyobb:
    if sor[0] > nagy:
        nagy = sor[0]
        tipus = sor[1]
        felsegjele = sor[2]
        rendszama = sor[3]
        meres = sor[4]
        
""" 
Jelenjen meg a mért legnagyobb sebesség, értelemszerűen a „túllépte”/”nem _lépte _túl”
szöveg, a jármű típusa, felségjele, rendszáma és a mérés ideje!
Ha több ilyen jármű is van, mindegyik adatait ki kell írni.
"""

print("3. feladat")
if nagy > 130 and tipus == "sz" or sor.jarmu_tipus == "m":
    print(f"{nagy} túllépte {tipus} {felsegjele} {rendszama} {meres}")
elif nagy > 100 and tipus == "b":
   print(f"{nagy} túllépte {tipus} {felsegjele} {rendszama} {meres}")
elif nagy > 80 and tipus == "t":
   print(f"{nagy} túllépte {tipus} {felsegjele} {rendszama} {meres}")
else:
    print(f"{nagy} nem_lépte_túl {tipus} {felsegjele} {rendszama} {meres}")


"""4. Hány magyar rendszámú jármű haladt el valamelyik traffipax mellett? A többször szereplő
rendszámokat csak egyszer kell figyelembe venni!"""
print()
print("4. feladat")
magyarok = []

for sor in lista:
    if sor.felseg_jel == "H":
        magyarok.append(sor.rendszam)

statisztika = dict()

for re in magyarok:
    statisztika[re] = statisztika.get(re, 0) + 1

nem_ismetlodo_rendszamok = len([rendsz for rendsz, db in statisztika.items() if db == 1])

print(str(nem_ismetlodo_rendszamok) + "\n")

"""
5. A C mérési ponton útjavítás miatt 09:00:00 és 13:00:00 között (a határokat is beleértve)
csak 110 km/h volt a megengedett sebesség. A 130-as korlátot betartó személyautók közül melyek lépték túl ezt a csökkentett sebességet?
Az érintett autók felségjelét, rendszámát, sebességét és a mérés időpontját kell kiírni.
"""
print("5. feladat")

for sor in lista:
    if sor.meres_helye == "C":
        if "09:00:00" <= sor.meres_ideje <= "13:00:00":
            if sor.sebesseg > 110 and tipus == "sz":
                print(f"{sor.felseg_jel} {sor.rendszam} {sor.sebesseg} {sor.meres_ideje}")
            
"""6. Néhány autós csak a traffipaxoknál lassít, különben „hasít”. Melyek azok a személyautók,
amelyeknek két szomszédos mérési pont közötti átlagsebessége nagyobb a megengedett
sebességnél? (Feltételezhetjük, hogy ha egy jármű bármely két mérési pontnál megjelent,
közben nem tért le az adott autópályáról – az esetleges letéréseket nem kell vizsgálni. A
pálya a legrövidebb és egyben a leggyorsabb útvonal.)
Jelenjen meg az érintett autók felségjele, rendszáma, a két ellenőrző pont azonosítója és a
jármű átlagsebessége.
Ha egy személyautó mindhárom mérési pont mellett elhaladt, akkor mindkét útszakaszra
vizsgálni kell a sebesség túllépését, és megjeleníteni az adatokat."""

"""7. Melyek azok a járművek, amelyek mindhárom ellenőrző pontnál megjelentek? Az A és C
mérőhelyek közötti átlagsebességük megfelelő volt-e? („igen” vagy „nem”)
Az autók felségjele és rendszáma is jelenjen meg!"""



    