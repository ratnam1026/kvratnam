a = input()
s1=""
count = 0
for i in a:
    count += 1
print ("the length of a is", count)
print ("the reverse of the string is", a[::-1])
for i in a:
    j = ord(i)
    if j >= 65 and j <= 90:
        i = chr(j+32)
        s1=s1+i
    if j >= 97 and j <= 122:
        i = chr(j-32)
        s1=s1+i
print(s1)
