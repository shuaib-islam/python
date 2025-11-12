file=open('codingal.txt', 'r')

print(file.read())

file.close()

file = open('codingal.txt' , 'w')

file.write("Hello, This is Shuaib, I am a student in grade VI and i am learning how to do 2D and 3D animation and Phython.")

file.close()

file = open('codingal.txt', 'a')
file.write("I love playing survival games , drawing which is why I like animation because it feels like your picture moving on its own.")
file.close()