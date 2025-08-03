# 1.
fruits = {"apple", "banana", "mango"}
fruits.add("orange")
fruits.remove("banana")
print("Fruits Set:", fruits)

# 2. 
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
common = set1.intersection(set2)
print("Common Items:", common)

# 3.
marks = {"Math": 90, "Science": 85, "English": 88}
marks["History"] = 92
print("Marks Dictionary:", marks)

# 4. 
numbers = [1, 2, 3, 4, 5]
cube_dict = {num: num**3 for num in numbers}
print("Cube Dictionary:", cube_dict)

# 5. 
for subject, mark in marks.items():
    print("Subject:", subject, "| Marks:", mark)



# 1. 
set_a = {"apple", "banana", "cherry"}
set_b = {"banana", "cherry", "date"}

print("Union:", set_a.union(set_b))
print("Intersection:", set_a.intersection(set_b))
print("Difference (A - B):", set_a.difference(set_b))

# 2.

word = "banana"
frequency = {char: word.count(char) for char in set(word)}
print("Character Frequency:", frequency)

#3.
students = ["goutham", "haji", "manoj"]
name_length = {name: len(name) for name in students}
print("Name-Length Dictionary:", name_length)
 
