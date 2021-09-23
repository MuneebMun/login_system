#importing module
import module

print("hello")

if True: 
    print("It is true")
else: 
    print ("FALSE")

print("another")

# List this can be modified
days = ['Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday']
print(days[1:3])

#Tuple this is read-only and starts with parenthesis
tuple = ("abc","gac")
print(tuple)

#dict
dict = {'name': 'hello world','code': '781'}
print(dict)
print(dict.keys())

#Defining a function 
def printMyName(name): 
    myname = "my name is %s" % name
    print(myname)
    return
    
printMyName("muneeb")

def print_module_data():
    module.print_func()

print_module_data()

str = raw_input("Enter your input")
print("received input", str)