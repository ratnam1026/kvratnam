import random
A5=[random.randint(30,60) for i in range(20)]
#print (A5)
A5.sort()
print (A5)
A6=[random.randint(1,30) for i in range(20)]
#print (A6)
A6.sort()
print (A6)
A7 = A5 + A6
def msort(x):
    result = []
    if len(x) < 2:
        return x
    mid = int(len(x)/2)
    y = msort(x[:mid])
    z = msort(x[mid:])
    while (len(y) > 0) or (len(z) > 0):
        if len(y) > 0 and len(z) > 0:
            if y[0] > z[0]:
                result.append(z[0])
                z.pop(0)
            else:
                result.append(y[0])
                y.pop(0)
        elif len(z) > 0:
            for i in z:
                result.append(i)
                z.pop(0)
        else:
            for i in y:
                result.append(i)
                y.pop(0)
    return result


    
r = msort(A7)
print(r)
print(len(r))
