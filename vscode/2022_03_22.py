#https://www.acmicpc.net/problem/3046
a = input().split()
print(int(a[1])*2 - int(a[0]))

#https://www.acmicpc.net/problem/3047
a = list(map(int, input().split()))
b = input()
A = min(a)
C = max(a)
for i in a:
    if i != A and i != C:
        B = i
        break
N1, N2, N3 = 0, 0, 0
LI = [N1, N2, N3]
for i in range(0, 3):
    if b[i] == "A":
        LI[i] = str(A)
    elif b[i] == "B":
        LI[i] = str(B)
    else:
        LI[i] = str(C)
print(" ".join(LI))

#https://www.acmicpc.net/problem/4447
a = int(input())
li = []
for i in range(0, a):
    b = input()
    n1 = b.count("g") + b.count("G")
    n2 = b.count("b") + b.count("B")
    if n1 == n2:
        li.append(b + " is " + "NEUTRAL")
    elif n1 > n2:
        li.append(b + " is " + "GOOD")
    else:
        li.append(b + " is " + "A BADDY")
print("\n".join(li))

#https://www.acmicpc.net/problem/1037
a = input()
b = list(map(int, input().split()))
c = max(b)
d = min(b)
print(c * d)