#https://www.acmicpc.net/problem/2108
a = int(input())
li = []
dic = {}
for i in range(0, a):
    b = int(input())
    li.append(b)
    if b in dic:
        dic[b] += 1
    else:
        dic[b] = 1
li = sorted(li)
print(round(sum(li)/a))
print(li[a//2])
maxvalue = [k for k,v in dic.items() if max(dic.values()) == v]
if len(maxvalue) > 1:
    print(sorted(maxvalue)[1])
else:
    print(maxvalue[0])
print(abs(li[-1] - li[0]))

#acmicpc.net/problem/1063
import sys
king_lo, stone_lo, count = map(str, sys.stdin.readline().split())

king_x = ord(king_lo[0]) - 64
king_y = int(king_lo[1]) 
stone_x = ord(stone_lo[0]) - 64
stone_y = int(stone_lo[1]) 

count = int(count)

move = {"R" : [1, 0], "L" : [-1, 0], "B" : [0, -1], "T" : [0, 1], "RT" : [1, 1], "LT" : [-1, 1], "RB" : [1, -1], "LB" : [-1, -1]}

for i in range(0, count):
    mo = input()
    if (king_x + move[mo][0] != stone_x or king_y + move[mo][1] != stone_y):
        if 0<king_x + move[mo][0]<9 and 0<king_y + move[mo][1]<9:
            king_x += move[mo][0]
            king_y += move[mo][1]
    else:
        if 0<stone_x + move[mo][0]<9 and 0<stone_y+move[mo][1]<9:
            king_x += move[mo][0]
            king_y += move[mo][1]
            stone_x += move[mo][0]
            stone_y += move[mo][1]
print(chr(king_x + 64) + str(king_y))
print(chr(stone_x + 64) + str(stone_y))

