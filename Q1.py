#Question 01

#program to print left Half Pyramid
rows = int(input("Enter the number of rows: "));
k = 1
for i in range(0, rows):  
     for j in range(0, k):
        print("*", end=' ')
     k = k+1
     print()

     
# program to Print onr more star pattern Pyramid
print("Program to print star pattern: \n");
rows = input("Enter maximum stars you want display on a single line :")
rows = int(rows) 
for i in range(0, rows):
    for j in range(0, i + 1):  
        print("*", end=' ')  
    print("\r")  
for i in range(rows, 0, -1):  
    for j in range(0, i - 1):  
        print("*", end=' ')  
    print("\r")
