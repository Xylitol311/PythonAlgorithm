def solution(numbers, hand):
    result = []
    Left_thm = 0
    Right_thm = 0
    Left_dis = 0
    Right_dis = 0
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            result.append("L")
            Left_thm = i
        elif i == 3 or i == 6 or i == 9:
            result.append("R")
            Right_thm = i
        elif i == 0:
            if Left_thm == 0 or Left_thm == 8:
                Left_dis = 1            
            elif Left_thm == 5 or Left_thm == 7:
                Left_dis = 2                
            elif Left_thm == 2 or left_thm == 4:
                Left_dis = 3            
            elif Left_thm == 1:
                Left_dis = 4
            
            if Right_thm == 0 or Right_thm == 8:
                Right_dis = 1
            elif Right_thm == 5 or Right_thm == 9:
                Right_dis = 2
            elif Right_thm == 2 or Right_thm == 6:
                Right_dis = 3
            elif Right_thm == 3:
                Right_dis = 4
            
            if Left_dis < Right_dis:
                result.append("L")
                Left_thm = 0
            elif Left_dis == Right_dis:
                if hand == "right":
                    result.append("R")
                    Right_thm = 0
                else:
                    result.append("L")
                    Left_thm = 0
            else:
                result.append("R")
                Right_thm = 0
        else:
            #i가 2,5,8일 때 엄지와의 거리의 절댓값을 구해서 더 가까운 쪽을 입력 abs(x) 함수 사용할 것.
            if abs(i - Left_thm) == 1 or abs(i - Left_thm) == 3 or abs(i - Left_thm) == 8:
                Left_dis = 1         
            elif abs(i - Left_thm) == 2 or abs(i - Left_thm) == 4 or abs(i - Left_thm) == 6:
                Left_dis = 2                
            elif abs(i - Left_thm) == 5 or abs(i - Left_thm) == 7:
                Left_dis = 3            
            
            if abs(i - Right_thm) == 1 or abs(i - Right_thm) == 3 or abs(i - Right_thm) == 8:
                Right_dis = 1         
            elif abs(i - Right_thm) == 2 or abs(i - Right_thm) == 4 or abs(i - Right_thm) == 6:
                Right_dis = 2                
            elif abs(i - Right_thm) == 5 or abs(i - Right_thm) == 7:
                Right_dis = 3

            if Left_dis < Right_dis:
                result.append("L")
                Left_thm = i
            elif Left_dis == Right_dis:
                if hand == "right":
                    result.append("R")
                    Right_thm = i
                else:
                    result.append("L")
                    Left_thm = i
            else:
                result.append("R")
                Right_thm = i
    print(result)
    
    answer = ''.join(result)
    return answer