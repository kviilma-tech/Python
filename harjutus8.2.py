# 03.12 Kaspar Viilma


telefonid={
'Mari': '5957503',
'Toomas': '5719979',
'Kertu': '5201750',
'Siim': '5580027',
'Piret': '5960799',
'Jaan': '5160415',
'Lea': '5760164',
'Mart': '5337951',
'Anni': '5004818',
'Tõnu': '5721873',
'Kai': '5811884',
'Rasmus': '5859489',
'Eva': '5039393',
'Oskar': '5635812',
'Liina': '5696114',
'Peeter': '5560756',
'Sandra': '5257415',
'Heiki': '5207248',
'Kristi': '5703338',
'Urmas': '5400549'
}

print(telefonid["Rasmus"])
telefonid["Kaspar"] = "6656566545"
del telefonid["Kristi"]
telefonid["Eva"] = "6656566545"
print(telefonid)

otsi = input("Otsi: ")
try:
   print(telefonid[otsi])
except:
      print("Otsitavat nime ei leitud")
      
      
      