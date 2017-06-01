li = [24,12,56,48,05,23,59]
k = len(li)
print("length of list is :",k)
for i in range(0,k):
  for j in range(i+1,k):
      if(li[i]>li[j]):
        temp=li[i]
        li[i]=li[j]
        li[j]=temp
for i in range(0,k):
  print(li[i])
