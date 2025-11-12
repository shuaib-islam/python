file = open('Codingal.txt', 'r')


Count = 0

readfile = file.read()

coList =  readfile.split("\n")

for i in coList:
    
    if i:
        Count += 1
        
print("The number of lines in the file: ")
print(Count)