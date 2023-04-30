#https://www.acmicpc.net/problem/9012
count = int(input())
for i in range(0, count):
    li = []
    st = input()
    for r in range(0, len(st)):
        if st[r] == "(":
            li.append("(")
        elif st[r] == ")":
            if "(" in li:
                li.pop()
            else:
                li.append("0")
                break
    if len(li) == 0:
        print("YES")
    else:
        print("NO")

#https://www.acmicpc.net/problem/1874

count = int(input())
li = []
st = []
state = True
c = 1
for i in range(0, count):
    num = int(input())
    while c <= num:
        li.append(c)
        st.append("+")
        c += 1

    if li[-1] == num:
        li.pop()
        st.append("-")
    else:
        state = False
        break
if state == True:
    for i in st:
        print(i)
else:
    print("NO")