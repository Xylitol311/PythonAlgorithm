from unittest import result


def solution(s):
    
    result = []
    print(len(s))
    for i in range(1, int((len(s)/2)) + 1):
        b = ''
        cnt = 1
        tmp = s[:i]
        
        for j in range(i, len(s), i):
            if tmp == s[j:j+i]:
                cnt += 1
            else:
                if cnt != 1:
                    b = b + str(cnt) + tmp
                else:
                    b = b + tmp
                cnt = 1
                tmp = s[j:j+i]
                print("현재 j, i : ", j, j+i)
        print("마지막 tmp : ", tmp)
        if cnt != 1:
            b = b + str(cnt) + tmp
        else:
            b = b + tmp
        print(b)
        result.append(len(b))
            
    return min(result)
print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))