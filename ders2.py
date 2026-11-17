#1
student = {
    "name": "Cavid",
    "age": 22,
    "major": "Computer Engineering"
}
print(student)

#2
student = {"name": "Cavid", "age": 22, "city": "Baku"}
print(student["name"])
print(student["age"])

#3
product = {"name": "Book", "price": 10}
new_price = float(input("Enter the new price: "))
product["price"] = new_price
print(product)

#4
user = {"name": "Murad", "age": 21, "phone": "0501234567"}
print(user["phone"])

#5
book = {
    "title": "Martin Eden",
    "year": 1970
}
book["author"] = "Cek London"
print(book)

#6
student = {"name": "Aysel", "age": 19}
student["email"] = "aysel@gmail.com"
print(student)

#7
products = {
    "laptop": 1900,
    "phone": 700,
    "tablet": 1000
}
products["phone"] = 900
print(products)

#8
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
student = {
    "name": name,
    "age": age,
    "city": city
}
print(student)

#9
student = {"name": "Nicat", "age": 20, "score": 85}
if student["score"] >= 50:
    print("Passed")
else:
    print("Failed")

#10
product_name = input("Enter the product name: ")
price = float(input("Enter the price: "))

product = {
    "name": product_name,
    "price": price
}
if product["price"] > 100 :
    print("Expensive product")
else:
    print("Cheap product")

#1
fruits = ("apple", "banana", "pear", "orange", "grape")
print(len(fruits))

#2
numbers = (5, 2, 5, 7, 5, 9, 2)
print(numbers.count(5))

#3
cities = ("Baku", "Ganja", "Sheki", "Gabala", "Sumgait")
print(cities.index("Sheki"))

#4
fruits = ("apple", "banana", "pear", "strawberry", "pomegranate")

fruit = input("Enter a fruit: ")

print(fruit in fruits)

#5
word = input("Enter a word: ")
print(word.upper())
print(word.lower())

#6
text = "python programming language"
print(text.capitalize())
print(text.title())

#7
name = input("Enter your name: ")
print(name.strip())

#8
text = "I am learning Python. Python is an interesting programming language."

text = text.replace("Python", "Java")
print(text)

#9
sentence = input("Enter a sentence: ")
words = sentence.split()
print(words)

#10
words = ["I", "am", "learning", "Python"]
sentence = " ".join(words)
print(sentence)


#1
try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError:
    print("Invalid input! Please enter a number.")

#2
try:
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    print(number1 / number2)
except ZeroDivisionError:
    print("Error, Cannot divide by zero")

#3
my_list = [10, 20, 30, 40, 50]
try:
    index = int(input("Enter an index: "))
    print(my_list[index])
except IndexError:
    print("Error! Index out of range.")
except ValueError:
    print("Invalid input! Please enter an integer.")

#4
students = {
    "Ali": 85,
    "Alsu": 90,
    "Cavid": 78
}
key = input("Enter a student name: ")
try:
    print(students[key])
except KeyError:
    print("Error, Student not found")

#5
try:
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    total = number1 + number2
    print("Sum:", total)
except ValueError:
    print("Invalid input! Please enter numbers.")

#6 ?
numbers = [10, 20, 30, 40, 50]
try:
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    index = int(input("Enter an index: "))
    print(number1/number2)
    print(numbers[index])
except (ValueError,ZeroDivisionError) :
    print("Invalid input! Please enter valid numbers.")
except IndexError:
    print("Error! Index out of range.")

#7 ?
try:
    filename = input("Enter the file name: ")

except FileNotFoundError:
    print("Error! File not found.")

#8
try:
    number = float(input("Enter a number: "))
    square = number ** 2

except ValueError:
    print("Invalid input, Please enter a number")
else:
    print("Square:", square)
    print("Operation completed successfully")

#9

try:
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    print("Result:", number1 / number2)
except ZeroDivisionError:
    print("Error! Cannot divide by zero.")
except ValueError:
    print("Invalid input! Please enter numbers.")
finally:
    print("Program finished.")

#10

try:
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    operator = input("Enter an operator (+, -, *, /): ")
    if operator == "+":
        print("Result:", number1 + number2)

    elif operator == "-":
        print("Result:", number1 - number2)

    elif operator == "*":
        print("Result:", number1 * number2)

    elif operator == "/":
        print("Result:", number1 / number2)

    else:
        print("Invalid operator!")

except ValueError:
    print("Invalid input! Please enter numbers.")

except ZeroDivisionError:
    print("Error! Cannot divide by zero.")



#Class
class Mehsul :
    def __init__(self,marka,model,il) :
        self.marka=marka
        self.model=model
        self.il=il
    def get_info(self) :
        print(self.marka,self.model,self.il)


# cLASS homework 1
class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages
book1 =Book("Python", "Alsu", 170) 
print(book1.name)
print(book1.author)
print(book1.pages)

#2
class Student:
    def __init__(self, name, age, surname):
        self.name = name
        self.age = age
        self.surname = surname
student1 = Student("Alsuska", 19, "G")
student2 = Student("Leyla", 21, "Huseynova")
student3 = Student("Murad", 18, "Mammadli")
print(student1.name, student1.age, student1.surname)
print(student2.name, student2.age, student2.surname)
print(student3.name, student3.age, student3.surname)

#3
class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    def get_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)

phone1 = Phone("Apple", "iPhone 17 pro ", 3800)
phone1.get_info()

#4
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)

car1 = Car("Mercedes", "S class", 2025)
car1.get_info()

#5
class Employee:
    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary

    def get_info(self):
        print("Name:", self.name)
        print("Surname:", self.surname)
        print("Salary:", self.salary)

employee1 = Employee("Alsu", " :( ", 30000)
employee1.get_info()

#6
class Library:
    def __init__(self, book_name, author):
        self.book_name = book_name
        self.author = author

    def get_info(self):
        print("Book:", self.book_name)
        print("Author:", self.author)

library1 = Library("Chess", "Stefan")
library1.get_info()

#7
class Game:
    def __init__(self, name, genre, price):
        self.name = name
        self.genre = genre
        self.price = price

    def get_info(self):
        print("Name:", self.name)
        print("Genre:", self.genre)
        print("Price:", self.price)

game1 = Game("Minecraft", "Random", 40)
game2 = Game("FIFA", "Sports", 70)
game1.get_info()
game2.get_info()

#8
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_info(self):
        print("Name:", self.name)
        print("Price:", self.price)
        print("Category:", self.category)

product1 = Product("PC", 1500, "Electronics")
product1.get_info()

#1

class Heyvan:
    def __init__(self,name):
        self.name=name
class It(Heyvan):
    pass
it=It("Totuska")
print(it.name)

#2
class Telebe:
    def __init__(self,name,group):
        self.name=name
        self.group=group

class MagistrTelebesi(Telebe):
    def __init__(self,name,group,ixtisas):
        super().__init__(name,group)
        self.ixtisas=ixtisas
student=MagistrTelebesi("Cavid","111","ce")
print(student.name)
print(student.ixtisas)
print(student.group)

#7
class Heyvan :
    def ses_cixar(self):
        print("Ses cixir")
class It(Heyvan):
    def ses_cixar(self):
        print("It hurur")
class Pisik(Heyvan):
    def ses_cixar(self):
        print("Pisik ses cixardir")
it1=It()
pisik1=Pisik()
it1.ses_cixar()
pisik1.ses_cixar()


#1
class Student :
    def __init__(self,name):
        self._name=name
    def get_name(self):
        return self._name
    def set_name(self,name):
        self._name=name
student1=Student("Ali")
print(student1.get_name())
student1.set_name("Mirze")
print(student1.get_name())

#2
class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    def get_balance(self):
        return self.__balance
    def set_balance(self,balance):
        if balance >= 0 :
            self.__balance=balance
        else :
            print("Invalid")

account1234=BankAccount(500)
print(account1234.get_balance())
account1234.set_balance(12566)
print(account1234.get_balance())

#1
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):

    def speak(self):
        print("Dog says: Woof!")


dog = Dog()
dog.speak()

    
#2
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass


class Cat(Animal):

    def speak(self):
        print("Cat says: Meow!")


class Cow(Animal):

    def speak(self):
        print("Cow says: Moo!")


cat = Cat()
cow = Cow()

cat.speak()
cow.speak()

#3
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car is starting")


class Motorcycle(Vehicle):

    def start(self):
        print("Motorcycle is starting")


car = Car()
motorcycle = Motorcycle()

car.start()
motorcycle.start()

#2

import math
number = 36
print(math.sqrt(number))
from math import sqrt
print(sqrt(number))

#3
import random as rnd
number = rnd.randint(1, 100)
print(number)

#4
def capitalize_text(text):
    return text.upper()

def count_words(text):
    return len(text.split())

#5
def show_product(name, price):
    print("Product:", name)
    print("Price:", price)

#6
