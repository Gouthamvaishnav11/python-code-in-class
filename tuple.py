
fruits = ("apple", "banana", "cherry")
more_fruits = ("mango", "apple")
print(len(fruits))                   
print( fruits + more_fruits)     
print( fruits * 2)                  
print('banana' in fruits)  
print(fruits[1])                   
print( fruits[0:2])                    
print( fruits.count("apple")) 
print( fruits.index("cherry"))  

num=(10,20,30,40,50,60)
print(num)
print("Length:", len(num))
print("Sum of elements:", sum(num))
print("Maximum value:", max(num))
print("Minimum value:", min(num))
print("First element:", num[0])
print("Last element:", num[-1])
print("Reversed tuple:", num[::-1])



# 1.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even numbers:", even_numbers)


# 2.
languages = ("Python", "Java", "C++")
language_list = list(languages)
language_list.append("Go")
languages = tuple(language_list)
print("Updated tuple:", languages)

# 3.
names = ["Alice", "Bob", "Charlie"]
name_lengths = [f"{name} ({len(name)})" for name in names]
print("Names with lengths:", name_lengths)
