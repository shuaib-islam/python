import sys

def intial_phonebook():
        rows, cols = int(input("Please enter intial contacts:" )), 5


        phone_book = []
        print(phone_book)
        for i in range(rows):
        
            temp = []
            for j in range(cols):
                if j == 0:
                    temp.append(str(input("Enter name*: ")))
                    if temp[j] == '     ':
                        sys.exit("Name is a mandatory feild. Process exiting due to blank feild")
                if j == 1:
                    temp.append(int(input("Enter number*: ")))
                    
                    
                if j == 2:
                    temp.append(str(input("Enter e-mail adress*: ")))
                    
                    if temp[j] == ' ' or temp[j] == '':
                            temp[j] = None
                    
                if j == 3:
                    temp.append(str(input("Enter date of birth(dd/mm/yy)*: ")))
                    
                    if temp[j] == ' ' or temp[j] == '':
                            temp[j] = None
                if j == 4:
                    temp.append(str(input("Enter category(Family/Friends/Work/Others)*: ")))
                    
                    if temp[j] == '  ' or temp[j] == '   ':
                            temp[j] = None
            phone_book.append(temp)
        print(phone_book)
        return phone_book