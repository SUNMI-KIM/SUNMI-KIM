#https://www.acmicpc.net/problem/15829
hashing = {"a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5, "f" : 6, "g" : 7, "h" : 8, "i" : 9, "j" : 10, 
           "k" : 11, "l" : 12, "m" : 13, "n" : 14, "o" : 15, "p" : 16, "q" : 17, "r" : 18, "s" : 19, 
           "t" : 20, "u" : 21, "v" : 22, "w" : 23, "x" : 24, "y" : 25, "z" : 26}
L = int(input())
Lstring = input()
hashingNum = 0

for i in range(0, len(Lstring)):
    hashingNum += hashing[Lstring[i]] * (31 ** i)
print(hashingNum % 1234567891)

#https://www.acmicpc.net/problem/2292
N = int(input())
room = 1
cnt = 1

while (N > room):
    room += 6 * cnt
    cnt += 1
print(cnt)