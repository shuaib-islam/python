new_file = open('new_file.txt', 'x')
new_file.close()

import os
print("Checking if my file exists or not...")
if os.path.exists('codingal.txt'):
    os.remove("codingal.txt")

else:
    print("The file does not exist")
    
my_file = open('codingal.txt', 'w')
my_file.write("Hello, This is Shuaib.")
new_file.close()

os.rmdir('Folder')
