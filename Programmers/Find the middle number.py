def solution(s):
    answer = ''
    if len(s) % 2 == 1:
        answer = s[len(s) // 2 : len(s) // 2 + 1]
    else:
        answer = s[len(s) // 2 - 1 : len(s) // 2 + 1]
    return answer
    # 다른 사람 답:
    # return s[(len(s) - 1) // 2 : len(s) // 2 + 1]


print(solution("power"))
print(solution("bridge"))
print(solution("bird"))
print(solution("Swift"))