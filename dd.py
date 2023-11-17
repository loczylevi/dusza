#A;F;12-02 20:30;22:00;4;1
"""
03-13 12:40 12-02 20:50 03-13 15:00
12-02 21:30 12-02 20:50 12-02 22:00
12-01 12:30 12-02 20:50 12-01 14:00
"""
a = "03-13"
veg = "03-13"
kezdeti = "12-02" 

if a < kezdeti < veg:
    print(f"ez az időpont {kezdeti} beleesik a két időpont közé")
else:
    print(f"ez az időpont {kezdeti} NEM beleesik a két időpont közé")