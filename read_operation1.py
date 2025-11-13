file = open('codingal.txt', 'r')
print(file.read())
file.close()

file = open('codingal.txt', 'r')
print("Opening first 15 character")
print(file.read(15))
file.close()