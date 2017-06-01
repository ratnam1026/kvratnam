# define n,k
n,k = 36,5

a,b = 0,1
for i in range(1,n):
    a,b = b,k*a+b
print (b)
