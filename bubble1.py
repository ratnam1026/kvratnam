a1 = [i for i in range(1,100+1)]
a2 = a1[::-1]

f = open("a3.txt", "r")
l = f.readline()
a5 = l.split(",")
a4 = list(map(int, a5))

def bub_sor(l):
  length = len(l)
  ctr = 0
  swapped = True
  while swapped:
    swapped = False
    for i in range(length-1):
      if l[i] > l[i+1]:
        l[i], l[i+1] = l[i+1], l[i]
        return l

print (bub_sor(a2))
