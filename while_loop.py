# 1. Write a python program to print "Saurab Shukla MySirG" five times!
i = 1;
while i<=5:
    print("Saurabh Shukla MySirG")
    i += 1;

# 2. Write a program to print first 10 natural number 
i = 1;
while i<=10:
    print(i, end=" ")
    i += 1;
print()

# 3. Write a python program to print first 10 natural number in reverse order 
x=1;
while x<=10:
    print(11-x, end=" ");
    x += 1;

#4. Write a python program to print first n even natural number 
print()
n = int(input("Please Enter how many even numbers you would like to print: "))
z =1 ;
while z<=n:
    print(2*z, end=" ")
    z += 1;

#4. Write a program to ask user to enter an even number at most 3 times. If user failed to enter an even number in all the three chances then he has lost the game. If user enter an even number, then no more chances will be given and announced him a winner.

print()

i_1 = 1;
while i_1<=3:
    if int(input("Enter an even number : "))%2!=0:
        print("That's wrong!")
        if i_1==3:
            print("You lost the game you entered 3 times non-even number!")
    else:
        print("You are a winner!")
        break
    i_1 += 1;


# continue 
z = 1;
z_1 = int(input("Enter a number : "))
while z<=10:
    if z_1%2==0:
        continue
    print(i,"z= ",z)
    i+=1;