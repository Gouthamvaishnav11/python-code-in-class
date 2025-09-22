#1
square = lambda x: x ** 2
print("Square of 5:", square(5))   



#2
def product_of_all(*args):
    product = 1
    for num in args:
        product *= num
    return product

print("Product:", product_of_all(2, 3, 4))   



#3
def user_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

user_profile(name="Renee", age=20, location="Warangal")



#4
def sum_natural(n):
    if n == 0:
        return 0
    else:
        return n + sum_natural(n - 1)

print("Sum of first 5 natural numbers:", sum_natural(5))   


#5
def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)

print("2^3 =", power(2, 3))   



from functools import reduce
list1=[1,2,3,4,5]
square=list(map(lambda x:x*x , list1))
print(square)

even=list(filter(lambda x:x%2 == 0 ,list1))
print(even)
sum =reduce(lambda x,y:x+y,list1)
print(sum)