# 케이스 t값
# 1000개 score 리스트
# 0~100 점  count = [0] *100
t = int(input())
mode_num = 0
for i in range(1, t+1):
    tc = int(input())
    score = map(int, input().split())
    count = [0] * 101
    for score_num in score:
        count[score_num] += 1
    max_count = max(count)
    for j in range(100, -1, -1):
        if count[j] == max_count:
            mode_num = j
            break
    print(f"#{tc} {mode_num}")