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

