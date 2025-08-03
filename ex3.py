numbers = list(range(1, 21))
squares = [x**2 for x in numbers]
odds = [x for x in numbers if x % 2 != 0]
print("Squares:", squares)
print("Odd Numbers:", odds)
