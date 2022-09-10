x = 25;
print(bin(x))
print(oct(x))
print(hex(x))
print(bin(5555555))
print(oct(555555))
# ord to find unicode 
print(ord("A"))
print(chr(65))
print(bin(-25))
a1,a2,a3,a4 = 1,2,3,4;
print(a3)
print(a4)
# print(5 in 4) #count error just because 4 is not iterable and in operator worrk only on iterable object
# Write a program to check whether a program is positive or negative 
x2 = int(input("Enter a number : "))
if(x2>0):
    print(f"{x2} is positive")
elif(x<0):
    print(f"{x2} is negative")
else:
    print("Enter number is not negative not positive that is 0")
# Write a program to print grade obtained in a test. Take marks obtained from user and display the grade 
marks_obtained = input("Enter the total marks out of 100 : ")
if (int(marks_obtained)<=100 and int(marks_obtained)>90):
    print("Grade A")
elif (int(marks_obtained)<=90 and int(marks_obtained)>80):
    print("Grade B")
elif(int(marks_obtained)<=80 and int(marks_obtained)>70):
    print("Grade C")
elif (int(marks_obtained)<=70 and int(marks_obtained)>60):
    print("Grade D")
elif (int(marks_obtained)<=60 and int(marks_obtained)>50):
    print("Grade E")
elif (int(marks_obtained)<=50 and int(marks_obtained)>=0):
    print("Grade F")
else:
    print("Kindly input the right marks out of 100")