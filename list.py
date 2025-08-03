# list functions
l1=[10,20,30,40]
l1.append(50)
l1.extend([60,70,80])
l1.pop()
print(l1.remove(50))
l1.insert(3,45)
print(len(l1))
l1.sort()
print(l1.index(45))
print(l1.count(40))

print(l1)

l2=["aaa","aaaa","a","aa"]
l2.sort(key=len)
print(l2)
l3=l2.copy()
print(l3)

# list comprehension
squares=[x*x for x in range(1,11)]
print(squares)
odd=[x for x in range(1,6) if x%2!=0]
print(odd)


