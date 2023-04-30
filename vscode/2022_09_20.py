import sys

count = int(input())
switch_list = list(map(int, sys.stdin.readline().split()))
length = len(switch_list)
number = int(input())
for i in range(0, number):
    one, two = map(int, sys.stdin.readline().split())
    if one == 1:
        r = 1
        two_clone = two
        while two < length+1:
            if switch_list[two-1] == 1:
                switch_list[two-1] = 0
            else:
                switch_list[two-1] = 1
            r += 1
            two = two_clone * r
    else:
        l = 0
        left = two-1
        right = two-1
        while switch_list[left] == switch_list[right]:
            if left - 1 > -1 and right + 1 < length and (switch_list[left-1] == switch_list[right+1]):
                left -= 1
                right += 1
                l += 1
            else:
                break
        if l == 0:
            if switch_list[two-1] == 1:
                switch_list[two-1] = 0
            else:
                switch_list[two-1] = 1
        else:
            for l in range(left, right+1):
                if switch_list[l] == 1:
                    switch_list[l] = 0
                else:
                    switch_list[l] = 1
i = 1
r = 20
l = 2
for k in switch_list:
    print(k, end=" ")
    i += 1
    if i > r:
        print()
        r = 20 * l
        l += 1
    
