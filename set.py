s1 = set()
s2 = {1,2,3}
s3 = {4,5,"Aftab", 5.7, 9.6}
print(s1,s2,s3,type(s1),type(s3), sorted(s2)) # sorted always gives list
s_1 = {1,2,3}
s_2 = {3,4,5}
s_3 = {1,2,3,4,5}
print(s_1.intersection(s_2))
print(s_1.union(s_2))
print(s_1.issubset(s_3))
print(s_2.issubset(s_2))
print(s_3.issuperset(s_1))
print(s_1.pop())
s_1.add(1)
print(s_1)
s_1.discard(1)
print(s_1)
s_1.remove(2)
print(s_1)