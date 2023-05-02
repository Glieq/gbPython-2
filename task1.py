n = int(input())
zero = 0
one = 0
for i in range(n):
    x = int(input())
if x == 0:
    zero += 1
else:
    one += 1
if one > zero:
    print(zero)
else:
    print(one)
