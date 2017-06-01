def isprime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return false
    for i in range(3,float(math.sqrt(n)+1),2):
        if n % i == 0:
            return False
        return True
