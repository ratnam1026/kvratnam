f = open("ini3.txt")

s = f.readline()
nums = f.readline()

print (s)
print (nums)

nums_arr = nums.split()
print (nums_arr)
a = int(nums_arr[0])
b = int(nums_arr[1])
c = int(nums_arr[2])
d = int(nums_arr[3])
print (a,b,c,d)

print (s[a:b+1], s[c:d+1])
