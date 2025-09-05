Week 3 – Object-Oriented Programming (OOP) in Python
Overview

This week focused on learning Object-Oriented Programming (OOP) in Python. OOP allows you to model real-world objects, organize code better, and make it reusable and maintainable.

Topics Covered

What is OOP?

Programming paradigm using classes and objects.

Helps structure programs using real-world concepts instead of just functions.

Classes & Objects

Class: blueprint for creating objects.

Object: instance of a class.

Example:

class Dog:
    def bark(self):
        print("Woof!")
my_dog = Dog()
my_dog.bark()


Constructor (__init__)

Initializes object attributes when an object is created.

Example:

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


Instance vs Class Variables/Methods

Instance: unique per object.

Class: shared across all objects.

Encapsulation

Protect data using _ (protected) or __ (private).

Use getters/setters to access private attributes safely.

Inheritance

Reuse code from another class.

Supports method overriding.

Example:

class Vehicle:
    def move(self): print("Vehicle moves")
class Car(Vehicle):
    def move(self): print("Car moves")


Multiple Inheritance & MRO

A class can inherit from multiple parents.

Python resolves conflicts using Method Resolution Order (MRO).

Polymorphism

Same interface, different implementations.

Duck typing and operator overloading.

Example: __add__, __str__.

Abstraction

Using abstract base classes to define methods that must be implemented in subclasses.

Example:

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


Composition vs Inheritance

Composition: class contains objects of other classes.

Inheritance: class derives from a parent class.

Mini Project

Library Management System

Classes: Book, Library, User

Features: add/remove books, issue and return books.

Concepts Applied: encapsulation, inheritance, polymorphism.

Key Takeaways

OOP makes code modular and reusable.

Use classes for structured modeling.

Understand when to use inheritance vs composition.

Practice real-world mini-projects to strengthen concepts.
