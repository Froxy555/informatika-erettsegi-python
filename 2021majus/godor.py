melysegek=[]
db=0
with open("melyseg.txt","r") as bemenet:
    for sor in bemenet:
        melysegek.append(int(sor.strip()))
        db+=1
print("1. feladat")
print("A fájl adatainak száma: ",len(melysegek))
print("2. feladat")
hely=int(input("Adjon meg egy távolságértéket! "))
print("Ezen a helyen a felszín",melysegek[hely-1],"méter mélyen van.")
print("3. feladat")
erintetlen=0
for i in melysegek:
    if i==0:
        erintetlen+=1;
print("Az érintetlen terület aránya: ","{:.2f}%".format((100*erintetlen)/db))
kimenet=open("godrok.txt",'w')
elozo=0;
egysor=[]
sorok=[]
godhosz=0
for ertek in melysegek:
    if ertek>0:
        egysor.append(str(ertek))
    if ertek==0 and elozo>0:
        sorok.append(egysor)
        egysor=[]
        godhosz+=1
    elozo=ertek
for egysor in sorok:
    print(" ".join(egysor), file=kimenet)
kimenet.close()
print("5. feladat")
print("A gödrök száma: ",godhosz)
print("6. feladat")
if melysegek[hely-1]==0:
    print("Az adott helyen nincs gödör.")
else:
    print("a)")
    poz=hely
    while melysegek[poz]>0:
        poz-=1
    kezdo=poz+2
    poz=hely
    while melysegek[poz]>0:
        poz+=1
    veg=poz
    print("A godor kezdete:",kezdo,"meter, a godor vege:",veg,"meter")
    print("b)")
    poz=kezdo+1
    while melysegek[poz]<=melysegek[poz-1] and poz<=veg:
        poz+=1;
    while melysegek[poz] >= melysegek[poz - 1] and poz <= veg:
        poz += 1;
    if poz>veg:
        print("Folyamatosan melyul")
    else:
        print("Nem melyul folyamatosan")
    print("c)")
    print("A legnagyobb melysege",max(melysegek[kezdo-1:veg]),"meter")
    print("d)")
    terfogat=10*sum(melysegek[kezdo-1:veg])
    print("A terfogata",terfogat,"m^3")
    print("f)")
    hossz=10*(veg-kezdo+1)
    print("A vízmennyiség",terfogat-hossz,"m^3")


