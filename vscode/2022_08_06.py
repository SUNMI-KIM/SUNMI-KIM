import math

def tof(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return True
    return False

a = int(input())
for i in range(0, a):
    b = int(input())
    if tof(b) == False:
        print(str(b) + " " + "1")
    else:
        for r in range(2, b+1):
            if b == 1:
                break
            count = 0
            sit = True
            while sit == True:
                if b%r == 0:
                    b = b // r
                    count += 1
                else:
                    sit = False
            if count > 0:
                print(str(r) + " " + str(count))

    