#Q2. How to reverse the words in a string in different ways?
#Way 1:
s1 ="etl qa labs"
#expected output : labs qa etl
l = s1.split()
#['etl', 'qa', 'labs']
ans =""
length = len(l)-1 #3-1 = 2
while length >=0:
    ans = ans + l[length]+" "
    # 1st iteration ans = " " +l[2] = labs
    # 2nd iteration ans = labs + l[1] = labs qa
    # 3rd iteration = labs qa + l[0] = labs qa etl
    length = length -1
    print(ans)
