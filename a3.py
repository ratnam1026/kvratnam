import random
A3=[random.randint(1,100) for i in range(100)]
print ("number of elements = ", len(A3))
print (type (A3))
print (A3)


f = open("a3.txt", "w")
A3_str = map(str,A3)
str_list = ",".join(A3_str)
print (str_list)
f.write(str_list)
f.close()
