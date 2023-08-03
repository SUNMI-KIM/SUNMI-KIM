#https://www.acmicpc.net/problem/10989
import sys

N = int(input())
num = [0] * 10001

for i in range(0, N):
    num[int(sys.stdin.readline())] += 1

for i in range(1, 10001):
    while (num[i] > 0):
        print(i)
        num[i] -= 1
 
#https://www.acmicpc.net/problem/2775
T = int(input())
for _ in range(T):
    k = int(input())  # input the floor number
    n = int(input())  # input the room number

    # Initialize the base case for the 0th floor
    room = [i for i in range(1, n+1)]

    # Calculate the number of people in each room for the given floor
    for _ in range(k):
        for j in range(1, n):
            room[j] += room[j-1]

    print(room[n-1])