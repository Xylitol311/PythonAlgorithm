def solution(id_list, report, k):
    # id_list만큼 0을 입력한 리스트 생성
    answer = [0] * len(id_list)    
    # 신고 당한 횟수를 저장할 사전 생성
    # id_list의 요소를 키로 사용하고 값은 0을 입력
    reports = {x : 0 for x in id_list}

    # reports에 ID별로 신고당한 횟수 입력(중복을 제거하기 위해 set 사용)
    for r in set(report):
        reports[r.split()[1]] += 1

    # reports에 입력된 횟수가 k 이상일 경우 answer 리스트에 해당하는 아이디 값에 +1
    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1
    # 최종 answer return
    return answer