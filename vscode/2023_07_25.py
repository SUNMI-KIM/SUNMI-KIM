#https://www.acmicpc.net/problem/10597

visited = [0] * 51
sequence = []
pre = [int(x) for x in str(input().strip())]

def check():
    for i in range(1, 51):
        if visited[i] == 1:
            index = i
            while index - i < len(sequence):
                if visited[index] == 0:
                    return False    
                index += 1            
            return True

def dfs(index):
    if index >= len(pre) - 1:
        if check():
            for ans in sequence:
                print(ans, end=" ")
            exit()
        return
    
    nxt = 0
    for length in range(1, 3):
        if index + length >= len(pre):
            return 
        nxt = nxt * 10 + pre[index + length]
        if nxt < 51 and not visited[nxt] and nxt != 0:
            visited[nxt] = 1
            sequence.append(nxt)
            dfs(index + length)
            sequence.pop()
            visited[nxt] = 0 

dfs(-1)