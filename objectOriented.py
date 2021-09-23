# class Employee: 
#     #class variable 
#     empCount = 12
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def printName(self):
#         print("My name is", self.name, "and my age is", self.age)
    
#     def printClassVariable(self):
#         print(Employee.empCount)

# emp1 = Employee("John",99)
# emp1.printName()
# emp1.printClassVariable()
# print("Printing completed")
# print(Employee.empCount,"abc")

# print(hasattr(emp1,'age'))


class Parent: 
    #data member 
    parentAttr = 20

    def __init__(self):
        print ("calling parent constructor")
    
    def setAttr(self,attr):
        Parent.parentAttr = Parent.parentAttr + attr
    
    def getAttr(self):
        print(Parent.parentAttr)

    def myMethod(self):
        print("this will be overridden")


#Inheriting parent class
class Child(Parent):
    def __init__(self):
        print("calling child constructor")
    
    def childMethod(self):
        print("calling child method")

    def myMethod(self):
        print("this will override parent")
    
#Since the Child class is derived from parent it will inherit its attribute you can use the attribute as it was defined in your class
c = Child()
print(c.setAttr(10))
print(c.getAttr())
print(c.parentAttr)
c.myMethod()