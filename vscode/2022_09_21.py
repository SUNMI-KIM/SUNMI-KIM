import sys
x, y = map(int, sys.stdin.readline().split())
z = int(100*y/x)

i = 0
if y/x == 1:
    print(-1)
elif int(100*y/x) == 99:
    print(-1)
else:
    one = z * x - 100 * y + x
    two = 99 - z
    if one % two == 0:
        print(int(one / two))
    else:
        print(int(one // two + 1))