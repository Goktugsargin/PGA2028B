hatasiz = False
while hatasiz == False:
    try:
        sayi = int(input("Bir tam sayı giriniz:"))
    except:
        print("Hatalı Girdi")
        hatasiz = False
    else:
        print("Sıkıntı YOK")
        hatasiz = True
    finally:
        print("girdi hatakontrolüne bağlı tutuldu")
    print(sayi)
