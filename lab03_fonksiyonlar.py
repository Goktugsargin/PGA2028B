def pi(): 
    return 3.14
def cemberincevresi (yaricap): 
    return 2*pi()*yaricap
def reklam(): 
    mesaj = "9B bu okulun en çalışkan sınıfıdır"
    print(len(mesaj)*"-")
    print(mesaj)
    print(len(mesaj)*"-")
def sinifBas (s, d):
    for say in range(d):
       print((say+1)*(s+" "))
r = int(input("Çembere ait yarıçap uzunluğunu giriniz:"))
print("Yarıçapı", r,"olan çemberin çevresi", cemberincevresi(r))
sinifBas ("9b",5)

 
reklam()
