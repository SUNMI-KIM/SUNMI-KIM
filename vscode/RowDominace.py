from glob import glob

global epi_va
global epi_dic
epi_dic = {}
epi_va = ""
def re(pi):
    pi1 = pi
    pi2 = pi
    if pi.count("2") > 0:
        return re(pi1.replace("2", "1", 1)), re(pi2.replace("2", "0", 1))
    else:
        epi_dic[epi_va].append(int(pi, 2))
        return int(pi, 2)

def solution(minterm):
    epi = []
    answer = []
    minterm_digit = minterm[0]
    minterm_count = minterm[1]
    minterm_set = set(minterm[2:])
    co = 0
    arr_reference = []
    arr = []
    arr1 = []
    arr2 = {}
    for i in range(0, minterm_digit+1):
        arr_reference.append([])
        arr.append([])
        arr1.append([])
    for r in range(2, len(minterm)):
        b = format(minterm[r], 'b')
        b = "0" * (minterm_digit - len(b)) + b
        arr[b.count("1")].append(b)
    while co < minterm_count:
        for i in range(len(arr)-1):
            for r in range(len(arr[i])):
                for k in range(len(arr[i+1])):
                    st = ""
                    cnt = 0
                    for l in range(minterm_digit):
                        one = arr[i][r][l]
                        two = arr[i+1][k][l]
                        if one == two :
                            st += one
                        else:
                            st += "2"
                            cnt +=1
                        if cnt > 1:
                            break
                    if len(st) == minterm_digit and st.count("2") == co+1 and cnt == 1:
                        if co == 0:
                            arr1[i].append(st)
                            arr2[st] = False
                        elif co >= 1:
                            arr2[arr[i][r]] = True
                            arr2[arr[i+1][k]] = True 
                            arr2[st] = False          
        if co == 0:
            arr = arr1
        elif co > 0:
            arr1 = arr
            arr = arr_reference
            for keys in sorted(arr2.keys()):
                if arr2[keys] == False:
                    arr[keys.count("1")].append(keys)
        co+=1
    for keys in sorted(list(set(arr2.keys()))):
        if arr2[keys] == False:
            answer.append(keys.replace("2", "-"))
            global epi_va
            epi_va = keys
            epi_dic[epi_va] = []
            re(epi_va)
    answer.append("EPI")
    epi_num = {}
    for values in list(epi_dic.values()):
        for r in values:
            if r not in epi_num.keys():
                epi_num[r] = 0
            else:
                epi_num[r] += 1
                
    for keys in epi_num.keys():
        if epi_num[keys] == 0:
            for one in epi_dic.keys():
                for two in epi_dic[one]:
                    if keys == two:
                        epi.append(one)
                        break
    for r in sorted(list(set(epi))):
        answer.append(r.replace("2", "-"))
    print(epi_dic)
    return answer

print(solution([4, 8, 0, 4, 8, 10, 11, 12]))