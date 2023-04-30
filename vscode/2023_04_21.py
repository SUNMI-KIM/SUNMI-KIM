#https://www.acmicpc.net/problem/2149
key = input()
password = input()
encryption = []
key_copy = sorted(key)
dic = {}

index = 0
for i in range(0, len(key)):
    encryption.append([])
    encryption[i].append(key_copy[i])
    dic[key_copy[i]] = 0
    for r in range(index, index + len(password)//len(key)):
        encryption[i].append(password[r])
    index += (len(password)//len(key))

encryption_sort = []
for i in range(0, len(key)):
    count = 0
    for r in range(0, len(encryption)):
        if count == dic[key[i]] and encryption[r][0] == key[i]:
            encryption_sort.append(encryption[r])
            dic[key[i]] += 1
            break
        elif encryption[r][0] == key[i]:
            count += 1

for i in range(1, len(encryption[0])):
    for r in range(0, len(key)):
        print(encryption_sort[r][i], end = "")

#https://www.acmicpc.net/problem/2870

M = int(input())

paper = []
for i in range(M):
    s = list(str(input()))
    for r in range(0, len(s)):
        if s[r].isdigit() and r == 0:
            paper.append(int(s[r]))
        elif s[r - 1].isdigit() and s[r].isdigit():
            save = int(paper.pop())
            paper.append((save * 10) + int(s[r]))
        elif s[r].isdigit():
            paper.append(int(s[r]))
paper.sort()
for i in paper:
    print(i)