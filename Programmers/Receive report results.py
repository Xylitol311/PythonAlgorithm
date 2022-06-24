from posixpath import split


def solution(id_list, report, k):
    answer = []
    user = {}
    cnt = {}
    report = list(set(report))
    
    for r in report:
        a, b = r.split()
        if a in user:
            user[a].append(b)
        else:
            user[a] = [b]
                
        if b in cnt:
            cnt[b] += 1
        else:
            cnt[b] = 1
    
    for id in id_list:
        result = 0
        try:
            for u in user[id]:
                if cnt[u] >= k:
                    result += 1
        except:
            result = 0
        answer.append(result)
    
    return answer


print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))