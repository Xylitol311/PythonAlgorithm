def solution(absolutes, signs):
    return sum(absolute if sign else -absolute for absolute, sign in zip(absolutes, signs))
    sum = 0
    for absolute, sign in zip(absolutes, signs):
        if sign:
            sum += absolute
        else:
            sum -= absolute
    return sum


    