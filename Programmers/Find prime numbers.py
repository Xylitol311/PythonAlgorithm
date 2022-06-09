def solution(n):
    answer = 0
    num_list = list(range(2, n + 1))
    for num_index in range(len(num_list)):
        if num_index == len(num_list):
            break
        for attempts in range(2, len(num_list) + 1):
            if num_list[num_index] * attempts in num_list:
                num_list.remove(num_list[num_index] * attempts)
    answer = len(num_list)
    return answer

print(solution(500000))