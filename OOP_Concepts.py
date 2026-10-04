#Q3.How to sum the ascii values for the given string?
# ASCII
s1 = "abc" # 97 + 98+99 = 294
sum = 0
for ch in s1:
    sum = sum +ord(ch)
    print(sum)