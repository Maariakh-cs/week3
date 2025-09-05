# Week 3: Object-Oriented Programming (OOP) in Python

## Overview
This week focuses on Object-Oriented Programming (OOP) concepts in Python and how to apply them in small projects.

## Topics Covered
- Classes & Objects
- Constructor (__init__)
- Instance & Class Variables/Methods
- Encapsulation
- Inheritance
- Polymorphism
- Abstraction
- Composition vs Inheritance

## Mini Project
**Library Management System**
- Classes: Book, Library, User
- Features: Add/remove books, issue/return books, track availability
- Concepts used: Encapsulation, inheritance, polymorphism

## Key Takeaways
- OOP makes code modular, reusable, and easy to maintain.
- Start with class design before writing methods.
- Use small projects to practice and reinforce concepts.
- Use classes for structured modeling.
- Understand when to use inheritance vs composition.
- Practice real-world mini-projects to strengthen concepts.

## OOP Revision Quiz (5 short coding tasks):
**Q1: Class & Object**
Create a class Animal with a method sound() that prints "Some sound".
Then create an object and call the method.

**Q2: Constructor**
Make a Student class with attributes name and grade.
When you create an object, it should print "Student <name> has grade <grade>".

**Q3: Inheritance**
Create a class Vehicle with a method move().
Then create a Car class that inherits Vehicle and overrides move() to print "Car is moving".

**Q4: Polymorphism (Operator Overloading)**
Create a class Vector with attributes x and y.
Overload the + operator (__add__) so that v1 + v2 adds the coordinates and returns a new Vector.
Print the result.

**Q5: Abstraction**
Use the abc module to make an abstract class Shape with an abstract method area().
Then create a Rectangle class that implements area().
