def solution(s):
    # 각 압축결과(문자열 길이)를 저장할 리스트 생성
    result=[]
    
    # 만약 문자열 길이가 1이면 그냥 1 return
    if len(s)==1:
        return 1
    
    # 반복할 수 있는 최대 길이인 (문자열 길이/2)로 범위를 지정하여 반복
    for i in range(1, (len(s)//2)+1):
        b = '' # 압축한 문자열을 저장할 str 변수
        cnt = 1 # 반복되는 문자열 단위의 횟수
        tmp=s[:i] # 확인할 문자열 단위

        for j in range(i, len(s), i): # tmp가 반복되는 지 확인하기 위한 반복문
            if tmp==s[j:i+j]: # 만약 다음 문자열 단위와 같다면 cnt에 +1
                cnt+=1
            else: # 다음 문자열 단위와 tmp가 다를 경우
                if cnt!=1: # 문자열 단위의 반복이 끝난 경우
                    b = b + str(cnt)+tmp # 기존 b에 반복횟수와 반복된 문자열 단위 추가
                else: # 문자열 단위의 반복이 없는 경우
                    b = b + tmp # 기존 b에 문자열 단위 입력
                tmp=s[j:j+i] # 그 다음 문자열 단위로 변경
                cnt = 1 # cnt 초기화
        # 모든 문자열을 돌고 내부 for문 반복이 끝난 경우
        if cnt!=1: 
            b = b + str(cnt) + tmp
        else:
            b = b + tmp
        # i 단위로 나누었을 때 문자열 길이를 result 리스트에 추가
        result.append(len(b))
    return min(result) # 가장 짧은 길이를 return