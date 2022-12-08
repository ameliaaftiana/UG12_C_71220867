angka=input("Masukkan angka : ")
dihitung=input("Masukkan angka yang dihitung : ")
ano=0
for i in list (angka):
   if i == dihitung:
    ano = ano+1
print("Angka",dihitung,"muncul sebanyak",ano,"kali.")