#Q1: How to print the characters from the string in different
s1 ="etlqa"
# Way 1
print("Way 1 :")
for ch in s1:
    print(ch)

#Way2
print("Way 2 :")
length = len(s1)
print(length)
for idx in range(length):
    print(idx,": ",s1[idx])

#way3
print("Way 3 :")
s1 = "etlqa"
i = 0
length = len(s1)
while (i < length):
    print(s1[i])
    i = i + 1