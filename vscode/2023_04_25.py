name = list(str(input()))
num = {}
ans = [" "] * (len(name))

for i in name:
    if i not in num:
        num[i] = 1
    else:
        num[i] += 1

for i in range(0, len(name) // 2 + 1):
    for r in sorted(num.keys()):
        if num[r] - 2 > -1:
            ans[i], ans[len(name) - 1 - i] = r, r
            num[r] -= 2
            break
        if num[r] == 1 and i == len(name) // 2:
            ans[i] = r
            break

flag = 1
for i in ans:
    if i == " ":
        print("I'm Sorry Hansoo")
        flag = 0
        break

if flag == 1:
    print("".join(ans))