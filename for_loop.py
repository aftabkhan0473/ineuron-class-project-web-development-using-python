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

print()
str2 = input("Enter the string : ");
for i in str2:
    if i=='r':
        break
    else:
        print(i)
else:
    print("All numbers are processed!")

#3. Write a program to print first n natural number

for i in range(int(input("How many natural number you would like to print ? "))):
    print(i+1, end=" ");

# 4. Write a program to print square of first n natural number 

print()
for i in range(int(input("How many first square number you would like to print : "))):
    print((i+1)**2, end=" ")

# 5. Write a program to print first n even natural number in reverse order 

print()
even_input = int(input("Enter a number : "));
for i in range(even_input):
    print((even_input-i)*2, end=" ")

# 6 Write a program to calculate sum of first n multiples of x

user_table_no = int(input("Enter a number : "))
user_multiple = int(input("Enter multiple one : "))
sum = 0;
for i in range(1,user_multiple+1):
    sum = sum + user_table_no*i;
print(sum)