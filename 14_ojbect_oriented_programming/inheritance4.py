#!/usr/bin/env python

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

class Student(Person):
    pass # used the pass keyword when you do not want to add any other properties or methods to the class
x = Student("Michael", "Jordan")
x.printname()
