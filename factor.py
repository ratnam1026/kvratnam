from math import sqrt
def factors(n):
    l = []
    for i in range(1,int(sqrt(n))+1):
        if n % i == 0:
            l.append(i)
            l.append(n//i)
    return (l)


n = 1
t = n
while 1:
    print (t)
    l = factors(t)
    if len(l) > 500:
        break;
    n += 1
    t += n


print (t)
