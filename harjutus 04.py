# #Ülesanded 4
# 
# Kingituste pakkimine
#     Sa töötad kingipoes ja sinu ülesanne on pakkida kingitusi.
#     Igasse kinkekarpi mahub täpselt 5 kingitust.
#     Sinu ülesandeks on arvutada, mitu täis kinkekasti saad teha ja mitu kingitust jääb üle, kui need kõik ei mahu karpidesse.
#     Loo programm, mis küsib kasutajalt, mitu kingitust on vaja pakkida.
#     Programm peaks seejärel arvutama, mitu täis kinkekasti saab teha ja mitu kingitust jääb üle. Kasuta täisarvulist jagamist (//) kinkekarpide arvu leidmiseks ja jäägi (%) operaatorit ülejäävate kingituste arvu leidmiseks.
#     Kasuta veakontrolli ja vastuse vormindamist
#     Näide:
#     Kasutaja sisestab: 23
#     Programm väljastab: Saad teha 4 täis kinkekasti. Üle jääb 3 kingitust.
#  ** astendamine // täisarvuline jagamine % jääk

maht = 5

try:
    kingitused  = int(input("Lisa kingituste arv:"))
    täis = kingitused // maht
    yle = kingitused % maht

    print(f"Saad teha {täis} täis kinkekasti. Üle jääb {yle} kingitust.")
except:
    print("Miski läks valesti!")
















# 
#  Raamatute allahindlus
#  Raamatupoes on 30% soodusmüük.
#       Kirjuta programm, mis küsib kasutajalt soovitud raamatute arvu ja arvutab nende kogumaksumuse,
# kui iga raamatu tavahind on 12,53€.
#       Väljasta lause, kasutades f-string vormindamist ja ümardamist 2 komakohta
#       Näide:
#       Kasutaja sisestab: 3
#       Programm väljastab: 3 raamatu hind soodustusega on 26.25€.


ale = 0.3
raamatute_arv = int(input("Soovitud raamatute arv: "))
hind = 12.53
summa = raamatute_arv * (hind-hind*ale)


print(f"4 raamatu hind soodustusega on  {summa:0.2f}€")




