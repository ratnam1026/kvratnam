import math
from my_lib import *



num=13195
primes=[2]
for i in range(3,math.sqrt(num),2):
    if isprime(i):
        primes.append(i)
    print (primes)
