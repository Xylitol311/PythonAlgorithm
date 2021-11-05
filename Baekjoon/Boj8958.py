num = int(input())
for i in range(num):
    txt = list(input())
    sum = 0
    cnt = 1
    for j in txt:
        if j == "O":
            sum += cnt
            cnt += 1
        else:
            cnt = 1
    print(sum)