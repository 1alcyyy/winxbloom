# calculator
first_num=int(input())
second_num=int(input())
operator=input("enter the operator : " )
if operator == "+" :
    print("solution = ", first_num + second_num)
elif operator == "-" :
    print("solution = ", first_num - second_num)
elif operator == "*" :
    print("solution = ", first_num * second_num)
elif operator == "/" :
    print("solution = ", first_num / second_num)
else:
    print("Invalid operator")

#Login System
correct_username="admin"
correct_password="123456"
enter_username=input()
enter_password=input()
if enter_username==correct_username and enter_password==correct_password :
    print("Login succesful")
if enter_username != correct_username and enter_password != correct_password :
    print("Invalid username and password")
elif enter_username!=correct_username:
    print("Invalid username")
elif enter_password != correct_password :
    print("Invalid password")

#Middle number
a=int(input()) # 6,7,9
b=int(input())
c=int(input())
if a>b and a<c:
    print(a)
elif b>a and b<c:
    print(b)
else:
    print(c)

#Triangle validity
a=int(input())
b=int(input())
c=int(input())
if a+b>c and b+c>a and a+c>b :
    print("Valid triangle")
else:
    print("Invalid triangle")

#ATM
balance=int(input())
withdraw=int(input())
if withdraw==0 or withdraw<0 :
    print("Invalid amount")
elif withdraw>balance :
    print("Insufficient balance")
else:
    print("new_balance = ", balance-withdraw)

#Electricity Bill
electricity_usage=float(input("Enter electricity_usage(kwH) : "  ))
if   100 >= electricity_usage >= 0 :
    print("Bill = ", electricity_usage*0.1, "AZN" )
elif 300>= electricity_usage >=101 :
    print("Bill = ", electricity_usage*0.15, "AZN")
else:
    print("Bill = ", electricity_usage*0.2, "AZN")

#Bonus Calculator
salary=int(input("Enter salary : "))
experience=int(input("Enter experience : "))
if experience>5 and salary<2000:
    print("bonus=", salary*0.2)
elif experience>5 and salary>=2000:
    print("bonus=", salary*0.15)
elif experience <=5 :
    print("bonus=", salary*0.1)

#Temperature
temp=float(input("Enter the temperature ('C ) : " ))
if temp>=30:
    print("Hot")
elif 30>temp>=15:
    print("Warm")
else:
    print("Cold")

#Cinema tickets (sual ver)
age=int(input("Enter your age : "))
student=input("Are you student ? : " )
ticket=15
if age<=12:
    print("Bill = " , ticket-ticket*0.5)
elif student=="Yes" :
    print("Bill = " , ticket-ticket*0.2)
elif age>=60:
    print("Bill = " , ticket-ticket*0.3)
else:
    print("No discount")

#Tax and salary 
salary=int(input())
if salary <1000:
    print("no tax")
elif 3000>salary>1000 :
    print("Tax = ", salary*0.1, "After tax = " , salary*0.1)
else:
    print("Tax = ", salary*0.2, "After tax = " , salary*0.2)

#The length of name
name=input("Enter your name : ")
print("Length = " , len(name))

#First and last letter
word=input("Enter a word : ")
if len(word)>=2 :
    print( word[0],word[-1])

#
word=input("Enter a word: ")
if "a" in word :
    print("Contains a")
else :
    print("No a")

#
name=input()
print(name.upper())

#
word=input("Enter your sentecne : ")
if "python" in word :
    print(word.replace('python','programming'))
else:
    print(word)

#
email=input("Enter your email : ")
if '@' in email and '.' in email :
    print("Valid email")
else :
    print("Invalid email")

#
word=input("Enter a  word : ")
if word[0]==word[-1] :
    print("Same")
else :
    print("Different")

# ***
username=input( "Enter a username : ")
if len(username)>=5 and " " not in username and "@" not in username :
    print("Valid username")
else :
    print("Invalid username")

#
n=int(input("Eded daxil edin : "))
for i in range(n) :
    print(i)

#
n=int(input())
for i in range(n,0,-1):
    print(i)

#
n=int(input())
for i in range(2,n+1,2,):
    print(i)

#n=int(input()) #n=4
total=0
for i in range(1,n+1,1) :  #1,5   1,2,3,4
    total=total+i #10
print(total)

#
n=int(input())
for i in range(2,n+1,2):
    print(i)

#
n=int(input())
for i in range(n,0,-1):
    print(i)

#
n=int(input())
total=0
for i in range(1,n+1,1):
    total=total+i
print(total)

#
n=int(input())
for i in range(1,n+1):
    if i%3==0:
        print(i)

# ***
for i in  range(5):
    n=int(input())
    if n>0 :
        print("Positive")
    elif n<0:
        print("Negative")
    else :
        print("Zero")

#
for i in range(10):
    n=int(input("Eded daxil edin : "))
    if n>5:
        print("Big")
    elif n<5:
        print("Small")
    else :
        print("Equal")

#
n=int(input("eded daxil edin : "))
for i in range(1,n+1):
    if i%15==0:
        print(i)

#
n=int(input("eded daxil edin : "))
for i in range(1,n+1):
    if i%5==0:
        print(i)

#
n=int(input())
total=0
for i in range(1,n+1):
    if i%2==0:
        total=total+1
print(total)

#
max_num=0
for i in range(5) :
    n=int(input())
    if n>max_num:
        max_num=n
print(max_num)

#
min_number=0
for i in range(5) :
    n=int(input("eded daxil edin : "))
    if min_number < n :
        min_number = n
print(min_number)

#
min_num = int(input())
for i in range(4):
    n = int(input())

    if n < min_num:
        min_num = n

print(min_num)

#
eded=int(input())
while eded >= 1:
    print(eded)
    eded=eded-1

#
n=int(input())
while n>=1  :
    if n%2==0 :
        print()

#
eded=0
while eded<= 5 :
    eded=eded+1
    print(eded)

#
eded=1
while eded <= 5 :
    print(eded)

eded=5
while eded >= 5 :
    print(eded)
    eded=eded-1

#
eded=1 
while eded<=100:
    print(eded)
    eded=eded+1

# + -
def musbet_menfi(eded) :
    if eded > 0 :
        return "Musbet"
    elif eded < 0 :
        return "Menfi"
    else :
        return "0-dir"
    
eded= int(input())
print(musbet_menfi(eded))

#
def yas_yoxlama(yas1) :
    if yas1 > 10 :
        print( " boyukdur ")
    else :
        print('10 dan kicikdir')
yas=int(input())
yas_yoxlama(yas)

#
def kvadrat_cemi (x,y):
    cem=x**2+y**2
    print(cem)
a=int(input())
b=int(input())
kvadrat_cemi(a,b)

#
def bolunme (a1,b1) :
    if a1 % b1 == 0 :
        print("bolunur")
    else :
        print("bolunmur")
a=int(input())
b=int(input())
bolunme(a,b)


###

adlar = ["Cavid", "Aylin", "Elnur"]
if len(adlar) > 0 :
    print("List doludur")
else :
    ad=input("Yeni ad daxil edin : ")
    adlar.append(ad)
print(adlar)

###

adlar= ( "aylin", "cavid" )
if len(adlar) > 0 :
    print("Tuple doludur")
else :
    yeni_telebe= adlar + ("alsu", "cavid")
print(yeni_telebe)

### in
adlar= [' Aysel',"Alsu",'Cavid','Elnur']
daxil_edilen_ad=input('Ad daxil edin : ')
if daxil_edilen_ad in adlar :
    print('daxil etdiyiniz ad tapildi')
else:
    print('daxil etdiyiniz ad tapilmadi')

###
meyveler=['yemis','qarpiz','nar','ciyelek']
daxil_edilen_meyve=input("Meyve adini daxil edin : ")
if daxil_edilen_meyve in meyveler :
    meyveler.remove(daxil_edilen_meyve)
    print(meyveler)
elif daxil_edilen_meyve not in meyveler :
    meyveler.append(daxil_edilen_meyve)
    print(meyveler)

#
name = input("Adinizi daxil edin: ")
name=name.upper()
name = name.lower()
name = name.capitalize()
print(name)

#
name = input("Adinizi daxil edin: ")
age = int(input("Yasinizi daxil edin: "))
user = {
    "ad": name,
    "yas": age
}
print(user)

#
telebe = {
    "name": "Alsu",
    "age": 19,
    "group": "P12",
    "city": "Baku"
}
print(telebe["name"])
telebe["age"] += 1
telebe["group"] = "P123"
telebe["city"] = "Ganja"
del telebe["age"]
print(telebe)