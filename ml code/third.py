# student have 5 subjects 
Std=int(input("Enter the std room number :"))
# list of five subjects number 
math=int(input("Enter the marks in math :"))
English=int(input("Enter the marks in english :"))
sci=int(input("Enter the marks in science :"))
soc=int(input("Enter the marks in social :"))
hindi=int(input("Enter the marks in hindi :"))

total_aggregate_marks =math +English+sci+soc+hindi
total_possible_marks=500
percentage=(total_aggregate_marks/total_possible_marks) *100


print("the aggregate marks of std :",total_aggregate_marks)
print("the percentage : ",percentage)




