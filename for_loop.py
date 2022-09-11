#1 Write a program to count "a" in a given string, using for loop
str1 = input("Enter a string in which you would like to find the number of a : ")

z=0
for i in str1:
    if(i=="a"):
        z+=1;
print("The total number of a in that string is  ",z)

# break 
for i in [1,2,3,4]:
    if i==3:
        break
    print(i, end=" ");

# 2. Print all the character of a string, but stop printing if 'r' appeared in the sequence, if all the character successfully printed the print message "All the characters aer processed."

str2 = input("Enter the string : ");
for i in str2:
    if i=='r':
        break
    else:
        print(i, end=" ")