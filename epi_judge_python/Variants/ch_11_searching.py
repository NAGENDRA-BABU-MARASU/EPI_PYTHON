import bisect

a = [0,1,2,3,4,5,6,7,8,9]

value = bisect.bisect_right(a, 5)

print(value)