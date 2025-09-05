'''class Computer:
    def __init__ (self):
        self.name = "M"
        self.age = 5
    def update(self):
        self.age = 5
    def compare(self, other):
        return self.age == other.age
c1=Computer()
c2=Computer()
c1.update()
c2.name="R"
if c1.compare(c2):
    print("Same")
else:
    print("Different")
print(c1.age)
print(c2.name)

class Car:
    wheels=4
    def __init__(self):
        self.mileage=10;
        self.company="BMW";
c1=Car()
c2=Car()
c1.mileage=8
Car.wheels=5
print(c1.mileage,c1.company,c1.wheels)
print(c2.mileage,c2.company,c2.wheels

class Student:
    school="XYZ School"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2      
        self.m3=m3
    def avg(self):
        return(self.m1+self.m2+self.m3)/3
    @classmethod
    def getSchool(cls):
        return cls.school
    @staticmethod
    def info():
        print("This is Student class..in OOPs.py")
s1=Student(34,47,32)
s2=Student(48,42,37)
print(s1.avg())
print(s2.avg())
print(Student.getSchool())
Student.info()

class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.Laptop()
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()
    class Laptop:
        def __init__(self):
            self.brand="HP"
            self.cpu="i5"
            self.ram=8
        def show(self):
            print(self.brand,self.cpu,self.ram)
s1=Student("M",2)
s2=Student("R",3)   
s1.show()
s2.show()

class A:
    def feature1(self):
        print("Feature 1 from A")
class B(A):
    def feature2(self):
        print("Feature 2 from B")
class C(B):
    def feature3(self):
        print("Feature 3 from C")
class D(A):
    def feature4(self):
        print("Feature 4 from D")
class E(C,D):
    def feature5(self):
        print("Feature 5 from E")
class F(E):
    def feature6(self):
        print("Feature 6 from F")
f1=F()
f1.feature1()
f1.feature2()
f1.feature3()
f1.feature4()
f1.feature5()
f1.feature6()

class A:
    def __init__(self):
        print("in A init")
class B(A):
    def __init__(self):
        super().__init__()
        print("in B init")
b1=B()

class A:
    def show(self):
        print("show A")
class B:
    def show(self):
        print("show B")
class C(A,B):
    pass
c1=C()
c1.show()
b1=B()
b1.show()

class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self, other):
        return Student(self.m1 + other.m1, self.m2 + other.m2)
    def __gt__(self, other):
        return (self.m1 + self.m2) > (other.m1 + other.m2)
    def __str__(self):
        return f"Marks: {self.m1}, {self.m2}"
s1=Student(50,60)
s2=Student(40,80)
s3=s1+s2
print(s3)
print(s1>s2)    
print(s2>s1)


class Demo:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            return a+b+c
        elif a!=None and b!=None:
            return a+b
        else:
            return a
d=Demo()
print(d.sum(5,9))
print(d.sum(5,9,6))
print(d.sum(5))

class A:
    def show(self):
        print("show A")
class B(A):
    def show(self):
        print("show B")
b1=B()
b1.show()
a1=A()
a1.show()

class Dog:
    def bark(self):
        print("The dog is barking.")
my_dog=Dog()
my_dog.bark()

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def introduce(self):
        print(f"Hi, I am {self.name} and I am {self.age} years old.")
s1=Student("M",22)
s1.introduce()

class Car:
    wheels=4
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def details(self):
        print(f"This is  a {self.brand} {self.model} with {Car.wheels} wheels.")
c1=Car("Toyota","Corolla")
c1.details()

class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
    def get_balance(self):
        return self.__balance
acc=BankAccount("M",5000)
acc.deposit(500)
print(acc.get_balance())

class Person:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
    def set_salary(self,amount):
        self.__salary+=amount
    def get_salary(self):
        return self.__salary
p1=Person("M",3000)
p1.set_salary(500)  
print(p1.get_salary()

class Vehicle:
    def move(self):
        print("This vehicle moves.")   
class Bike(Vehicle):
    def move(self):
        print("The bike is moving on 2 wheels")
b1=Bike()
b1.move())

class Father:
    def skills(self):
        print("Gardening, Cooking")
class Mother:   
    def skills(self):
        print("Art, Cooking") 
class Child(Father,Mother):
    pass
c1=Child()
c1.skills()

class Teacher:
    def work(self):
        print("Teaching")
class Doctor:
    def work(self):
        print("Healing")
for profession in [Teacher(),Doctor()]:
    profession.work()

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return Point(self.x + other.x, self.y + other.y)    
p1 = Point(2, 3)
p2 = Point(4, 5)
p3 = p1 + p2
print(p3.x, p3.y)

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14 * self.radius **2
c = Circle(5)
print(c.area())

class Engine:
    def start(self):
        print("Engine starts")
class Car:
    def __init__(self):
        self.engine=Engine()
    def drive(self):
        self.engine.start()
        print("Car is driving")
c1=Car()
c1.drive()

class Battery:
    def charge(self):
        print("Battery charges")
class Phone:
    def __init__(self):
        self.battery=Battery()
    def use(self):
        self.battery.charge()
        print("Using the phone")
p1=Phone()
p1.use()

class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.available=True
    def __str__(self):
        status = "Available" if self.available else "Issued"
        return f"{self.title} by {self.author} ({status})"
class Library:
    def __init__(self):
        self.books=[]
    def add_book(self,book):
        self.books.append(book)
    def show_books(self):
        for book in self.books:
            print(book)
class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
    def borrow_book(self, book, library):
        if book in library.books and book.available:
            book.available = False
            self.borrowed_books.append(book)
            library.books.remove(book)
            print(f"{self.name} borrowed {book.title}")
        else:
            print(f"{book.title} is not available")
    def return_book(self, book, library):
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)
            library.books.append(book)
            print(f"{self.name} returned {book.title}")
        else:
            print(f"{self.name} did not borrow {book.title}")
    def show_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name} has borrowed:")
            for book in self.borrowed_books:
                print(" -", book)
        else:
            print(f"{self.name} has not borrowed any books.")
b1=Book("1984","George Orwell")
b2=Book("To Kill a Mockingbird","Harper Lee")       
b3=Book("The Great Gatsby","F. Scott Fitzgerald")
lib=Library()   
lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)
lib.show_books()
u1=User("M")
u1.borrow_book(b1,lib)
u1.borrow_book(b2,lib)
lib.show_books()
u1.return_book(b1,lib)
lib.show_books()
u1.return_book(b3,lib)
u1.show_borrowed_books()'''

class Animal:
    def sound(self):
        print("Animal makes a sound")
a1=Animal()
a1.sound()

class Student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
    def display(self):
        print(f"Student {self.name} has grade {self.grade}.")
s1=Student("M",10)
s1.display()

class Vehicle:
    def move(self):
        print("Vehicle is moving")
class Car(Vehicle):
    def move(self):
        print("Car is moving")
c1=Car()
c1.move()

class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return Vector(self.x + other.x, self.y + other.y)
v1=Vector(2,3)
v2=Vector(4,5)
v3=v1+v2
print(v3.x,v3.y)

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length * self.breadth
r=Rectangle(4,5)
print(r.area()) 