num = int(input("Enter a five digit number: "))

last_digit = num % 10
fourth_digit = (num // 10) % 10
third_digit = (num // 100) % 10
second_digit = (num // 1000) % 10   
first_digit = (num // 10000)

reverse = (last_digit * 10000) + (fourth_digit * 1000) + (third_digit * 100) + (second_digit * 10) + (first_digit)
print("Reversed number is:", reverse)
