lst = ["Apple", "Banana", "Guava", "Mango", "Kiwi"]

print("length of list", len(lst))
print("First element of list",lst[0])
print("last element of the list", lst[-1])

lst.append("papaya")
print("After append papaya list", lst)

lst.remove("Guava")
print("After removing Guava list", lst)

lst.sort()
print("Sorted list", lst)

lst.pop(1)
print("After poping the element", lst)

lst.reverse()
print("Reversed list", lst)

print("Multiplication of list", lst*2)

lst = lst[:4]
print("sliced list", lst)

lst.clear()
print(lst)