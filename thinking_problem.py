# s = "1a2bc3" sum = 1+2+3 how?
s = "1a2b3c";
sum_b = 0;
for i in range(0,6,2):
    sum_b = sum_b + int(s[i]);
print(sum_b)