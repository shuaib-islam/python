# empty dictionaries

my_dict = {}

#dictionaries with integer key

my_dict ={ 1 : "Apple" , 2 : "ball"}

#dictionaries with mixed keys

my_dict ={"name" : "Jack" , 1 : [1,2,3,4,5]}
my_dict ={"name" : "Jack" , "age" : [12]}

# get items


print(my_dict["name"])
print(my_dict.get("age"))
 
# update the value

my_dict["age"] = 30

print(my_dict)

# add items
my_dict["gender"] = "male"
print(my_dict.get)

# remove element
my_dict.pop("age")
print(my_dict)

# remove all elements
my_dict.clear()

