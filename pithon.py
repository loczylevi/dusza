# fogalások adatai
##Vendég név, ||| Foglalás vagy lemondása (F vagy L karakter), ||| Foglalás kezdete (HÓNAP-NAP ÓRA:PERC formátumban), ||| Foglalás vége (ÓRA:PERC formátumban) A foglalás végének ugyanarra a napra kell esnie mint a kezdete, ||| Foglalt székek száma, ||| Foglalt asztalok azonosítója pontosvesszővel elválasztva

"""_______________________________________________"""
# asztalok
# azonosító ||| hány személyes az asztal (4, 6, vagy 8) ||| beltéri vagy kültéri asztal (B vagy K karakter) |||

class Asztalok:
    def __init__(self, sor):
        id, hany_szemely, elhelyezkedes = sor.strip().split(";")
        self.id = int(id)
        self.hany_szemely = int(hany_szemely)
        self.elhelyezkedes = elhelyezkedes

class Foglalasok:
    def __init__(self, sor):
        guest_name, fog_v_lem, kezdet, veg, szekek_szam, fog_id = sor.strip().split(";")
        self.guest_name = guest_name
        self.fog_v_lem = fog_v_lem
        self.kezdet = kezdet
        self.veg = veg
        self.szekek_szam = szekek_szam
        self.fog_id = fog_id


bemenet = "asztalok1.txt"

with open(bemenet, "r", encoding="UTF-8") as f:
    lista = [Asztalok(sor) for sor in f]





bekeres = input("""• Foglalás
• Foglalás törlése
• Statisztika
• Kilépés\nÍrja be az adott opciót: (F/FT/S/K)\t""")

#_______________________________________________________________

if bekeres == "F":
    print("\n<<< FOGLALÁS >>>\n")
    nev = input("Vendég neve:\t")
    f = "F"
    while True:
        #(HÓNAP-NAP ÓRA:PERC formátumban)
        #guest_name, fog_v_lem, kezdet, veg, szekek_szam, fog_id = sor.strip().split(";")
        kezdeti = input("Foglalás kezdete:\t")
        vege = input("Foglalás vége:\t")
        kezdeti_honap = kezdeti[0:2]
        kezdeti_nap = kezdeti[3:5]
        kezdeti_ora = kezdeti[6:]
        if "06:00" <= kezdeti_ora <= "22:00" and kezdeti_ora < vege and "06:00" <= vege <= "22:00":
            print("A foglalást 6:00 és 22:00 esik ergó jót adtál meg és a foglalás kezdete kisebb ming a végpont")
            break
        else:
            print("A foglalást NEM 6:00 és 22:00 között adtad meg  VAGY a foglalás kezdete nem kisebb ming a végpont ergó nem jó")
    
    #vege = kezdeti_honap + "-" + kezdeti_nap + " " + vege
    szekek_szama = input(" Foglalt székek száma:\t")
    helyileg = input("Beltéri vagy kültéri asztalt szeretne:\t")
    azon = 1

#_______________________________________________________________



with open("foglalas1.txt", "r", encoding="UTF-8") as f2:
    foglalas = [Foglalasok(sor) for sor in f2]


#_______________________________________________________________

fogalas_jo_e = False

for sor in foglalas:
    honap_dat = sor.kezdet[0:5] + " " +  sor.veg
    if sor.kezdet[0:5] <= kezdeti[0:5] <= honap_dat[0:5]:
        if sor.kezdet[6:] <= kezdeti[6:] <= sor.veg:
            pass
        else:
            print(f"ez jo idöpont {kezdeti}")
            fogalas_jo_e = True
            break
# ha nem létezik a hanopa akkor bugos
#_______________________________________________________________

    

elso = True
if fogalas_jo_e:
    print("Teljesíthető a foglalás!")
    file = open("foglalas1.txt", "a") 
    if elso:
        #guest_name, fog_v_lem, kezdet, veg, szekek_szam, fog_id = sor.strip().split(";")
        content = f"\n{nev};{f};{kezdeti};{vege};{szekek_szama};{azon}"
    else:
        content = f"{nev};{kezdeti};{vege};{szekek_szama};{helyileg}\n"
    file.write(content) 
    elso = False
    file.close() 
else:
    print("Nem teljesíthető a foglalás!")


