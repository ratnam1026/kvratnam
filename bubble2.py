f = open("a3.txt", "r")
l = f.readline()
#print (l)
a5 = l.split(",")
#print (type (a5))
#print (a5)
a4 = list(map(int, a5))
print (a4)
#print (sum(a4))
k = len(a4)
print("length of list is :",k)
for i in range(0,k):
  for j in range(i+1,k):
      if(a4[i]>a4[j]):
        temp=a4[i]
        a4[i]=a4[j]
        a4[j]=temp
for i in range(0,k):
  print(a4[i])
