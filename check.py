list1 = [1,2,3,4]
t1 = tuple(list1)
print(t1) # We can convert list into tuple!
input_tuple = tuple(int(e) for e in input("Enter number separated by comma : ").split(','))
print(input_tuple)