#PART 1 (4,9 subheli)
#1
a=float(input())
if a>0:
    print("Ədəd müsbət ədəddir")
elif a<0:
    print("Ədəd mənfi ədəddir")
else:
    print("Ədəd 0-a bərabərdir")


#2
a=int(input())
if a>=18:
    print("Yetkinsən")
else:
    print("Yetkin deyilsən")


#3
a=int(input())
if a%2==0:
    print("Ədəd cütdür")
else:
    print("Ədəd təkdir")


#4 
a=int(input())
if 100>= a >=0 : # burani sorus ! men bu if den asli sert qurmaq istemisem duzdu ya yox?
    if a >= 90:
        print("Əla")
    elif a>=60:
        print("Yaxşı")
    else:
        print("Zəif")

#


#5
age=int(input("Yaşınızı daxil edin : "))
salary=float(input("Əmək haqqını qeyd edin : "))
if age>18 and salary>500:
    print("Kredit verilə bilər")
else:
    print("Kredit verilə bilməz")


#6
n=input("Həftənin gününü daxil edin : ")
if n == "Şənbə" or n == "Bazar":
    print(" Həftə sonudur ")
else:
    print(" İş günüdür ")


#7
a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)


#8 
age=int(input())
permission=True
if age>=18:
    print("filme baxa bilersen.")
elif 18>age>14 and permission==True :  
    print("valideyn icazesi ile baxa bilersen.")
else:
    print("BAXMA!!!")


#9 (Sual ver sehv elemisen)
customer_type=input("Enter the type of subscription : ")
amount=float(input())
if customer_type=="VIP" and amount>100: # tutaq ki men inputa VIP yox vip verdim onda ??? nece duzeldim bu hisseni 
    print("discounted_price=", amount-amount*0.2 ) 
elif customer_type=="Regular" and amount>100:
    print("discounted_price=", amount-amount*0.1 )
else:
    print("discount = 0 %")


#10
age=int(input())
salary=float(input())
if age<18:
    print("kredit verilmir")
elif age>=18 and salary<500:
    print("az meblegde kredit verile biler")
else:
    print("yuksek meblegde kredit verile biler")

#11
num=1
while num<=100 :
    print(num)
    num=num+1

#
kod=int(input("kodu daxil edin : "))
while kod != '1234' :
    print("Yanlis kod daxil etdiniz")
    kod=int(input("kodu yeniden daxil edin : "))
print("Dogru kod daxil etmisiniz ")  



### DERS 2
### FOR 1
for i in range(1,11) :
    print(i)

#2
total=0
for i in range(1,51):
    total=total+i
print(total)

#3
for i in range(1,101):
    if i%7==0 :
        print(i)

# WHILE 1 
cem=0
eded=int(input())
while eded != 0 :
    cem=cem+eded
    eded=int(input())
print(cem)

#2
i=1
while i<= 100 :
    if i % 2 ==0 :
        print(i)
    i=i+1

#3
i=1
while 1<=100:
    print(i)
    i=i*2

# BREAK 1
for i in range(1,21) :
    print(i)
    if i == 10 :
        break

#2 ?
eded=int(input())
if eded<0 :
    break

#3 
cem=0
for i in range(1,110) :
    cem=cem+i
    if cem > 50 :
        break
print(cem)

# CONTINUE 1
for i in range(1,21) :
    if i % 2 != 0 :  # i % 2 == 1
        continue
    print(i)

#2
for i in range(1,31) :
    if i % 3 == 0 :
        continue
    print(i)

#3
for i in range(1,51):
    if i % 5 == 0:
        continue
    print(i)


# DEF 
#2
def ad_soyad(ad, soyad):
    print(ad + soyad)
a=input("adinizi daxil edin : ")
b=input("soyadinizi daxil edin : ")
ad_soyad(a,b)

#3
def email_yarat(ad, soyad):
    print(ad + '.' +soyad + "@gmail.com")
a=input("adinizi daxil edin : ")
b=input("soyadinizi daxil edin : ")
email_yarat(a,b)

#4
def kvadrat(eded):
    return eded ** 2
a=int(input("eded daxil edin : "))
print(a)

#5 
def hesabla(maas, bonus):
    return maas + bonus
a=float(input())
b=float(input())
print(hesabla(a,b))

#6
def orta(a, b, c):
    return (a + b + c) / 3
x=int(input())
y=int(input())
z=int(input())
print(orta(x,y,z))

#7
def qiymet_deyeri(bal):
    if 90 <= bal <= 100:
        print("Ela")
    elif 70 <= bal <= 89:
        print("Yaxsi")
    elif 50 <= bal <= 69:
        print("Kafi")
    elif 0 <= bal <= 49:
        print("Qeyri-kafi")
a=int(input(" Bal daxil edin : "))
qiymet_deyeri(a)

#8
def eded_yoxla(eded):
    if eded > 0:
        print("Musbet")
    elif eded < 0:
        print("Menfi")
    else:
        print("0")
a=float(input("Eded daxil edn : "))
eded_yoxla(a)

#9
def ededleri_cap_et():
    eded = 1
    while eded <= 10:
        print(eded)
        eded = eded + 1
ededleri_cap_et()

#10 
def sifre_yoxla():
    sifre = input("Sifreni daxil edin: ")
    while sifre 

#1
meyveler = ["alma", "banan", "armud", "nar"]

meyveler.remove("alma")

print(meyveler)

#2
adlar = ["Ali", "Aysel", "Murad"]
adlar.insert(0, "Leyla")
print(adlar)

#3
mehsullar = ["çörək", "süd", "pendir"]

yeni_mehsul = input("Yeni məhsul: ")

mehsullar.append(yeni_mehsul)

print(mehsullar)

#4
ededler = [10, 20, 30, 40]

silinen = ededler.pop()

print("Silinen element:", silinen)
print("Yeni siyahı:", ededler)

#5
ededler = [1, 2, 3, 4, 5, 6]
if len(ededler) > 5:
    print("List boyukdur")
else:
    print("List kiçikdir")

#6
meyveler = ["alma", "banan", "Python", "armud"]
if "Python" in meyveler :
    meyveler.remove("Python")
print(meyveler)

#7
adlar = ["Ali", "Aysel", "Murad"]
yeni_ad = input("Yeni ad: ")
adlar.insert(1, yeni_ad)
print(adlar)

#8
siyahi = [10, 20, 30, 40, 50]
for i in siyahi:
    print(i)

#9
ededler = [5, -3, 0, 8, -7]
for i in ededler:
    if i > 0:
        print("Musbett")
    elif i < 0:
        print("Menfi")
    else:
        print("Sifirr")

#10
ballar = [95, 82, 65, 45, 90, 55]
for bal in ballar:
    if bal >= 90:
        print("ela")
    elif bal >= 70:
        print("Yaxsi")
    elif bal >= 50:
        print("Kafi")
    else:
        print("Qeyri-kafi")
        

    