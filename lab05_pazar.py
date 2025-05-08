mesaj = "Pazar Listesi Yapıyorum."
sepet = []
agirlik = []

print(mesaj,"\n",len(mesaj)*'-',end="\n",sep="")

while (1==1):
    print("Poşetinizde ne var?")
    
    icerik = input("Poşet içeriğini giriniz: ")
    icerik = icerik.lower()
    if icerik == "boş":
        break
    varMi = False
    for icindeki in sepet:
        if icindeki == icerik:
            varMi = True            
            break
    miktar = float(input("Miktarını giriniz (kg): "))
    if varMi == False:
        sepet.append(icerik)
        agirlik.append(miktar)
    else:
        agirlik[sepet.index(icerik)]+=miktar
print("pazardan alınacaklar:")
for indis in range(len(sepet)):
    print(sepet[indis][0].upper(),sepet[indis][1:],"\t: ",agirlik[indis], " kg",sep="")
