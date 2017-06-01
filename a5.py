import random
A5=[random.randint(1,50) for i in range(20)]
#print (A5)
A5.sort()
print ("the sorted list of A5 is :", A5)
A6=[random.randint(51,100) for i in range(20)]
#print (A6)
A6.sort()
print ("the sorted list of A5 is :", A6)
print (A5 + A6)
