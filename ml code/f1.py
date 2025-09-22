def sumall(*args):
    return sum(args)

print(sumall(1,2,3,4))
print(sumall(1,2))
print(sumall(10,12,15,18,19))


def std(**details):
    for i, j in details.items():
        print("key =", i, "value:", j)

std(sno="1", name="goutham")


def greet():
    print("Hello, welcome!")

greet() 



def add(a, b):
    return a + b
print(add(2, 3)) 



def greet(name="User"):
    print("Hello", name)
greet("goutham") 
greet()         



def student(name, age):
    print("Name:", name)
    print("Age:", age)
student(age=21, name="goutham")




def total(*numbers):
    return sum(numbers)
print(total(1, 2, 3, 4)) 



def square(x):
    return x * x
result = square(5)
print(result) 




