[Ülesanne 5.py](https://github.com/user-attachments/files/23764984/Ulesanne.5.py)
# Kaspar Viilma
# 26.11.25
import random

# Mündiviskamise äraarvamine koos
# juhuslikkusega (and ja or)
# 0 - kiri
# 1 - kull
mynt = random.randint(0,1)
arvamus = int(input("Kull või kiri (0/1): "))
print(f"Münt: {mynt}")
print(f"Arvamus: {arvamus}")
if mynt == arvamus:
    print("VÕIT")
else:
    print("Kaotus")

# Ilmaennustuse rakendus (and)


try:
    temp = int(input("Sisesta kraadid C: "))
    if temp < 0:
        print("talveriided")
    elif temp >= 0 and temp <=15:
        print("kevad-sügis")
    else:
        print("suvi")
        

    
except:
    print("Urror - määää")
