# 최대 이익 값 출력
# 케이스  t 입력값
# 케이스 별 날짜수 N
# 날짜수 별 매매가 P[i]
# min(P) == P[N] : 최대이익 0
# if P[i] != max(P[i, N]): buy.append(P[i]) i++
# if buy[] == True && P[i] == max(P[i, N]): for j in range(len(buy)) sell[i] = P[i] - buy[j]
# print (f"#{t} {sum(sell)}")

# t = int(input())
# for i in range(1, t+1):
#     buy =[]
#     sell = 0
#     N = int(input())
#     P = list(map(int, input().split()))
#     if min(P) == P[N-1]:
#         print(f"#{i} {0}")
#     else:
#         for j in range(N):
#             if P[j] != max(P[j:N]):
#                 buy.append(P[j])
#             elif P[j] == max(P[j:N]):
#                 for num in buy:
#                     sell += int(P[j]) - int(num)
#                 buy = []
#         print(f"#{i+1} {sell}")

# 반대 순서로 풀면 쉬움 reversed
t = int(input())

for i in range(1, t + 1):
    N = int(input())
    P = list(map(int, input().split()))

    max_price = 0
    profit = 0

    for price in reversed(P):
        if price > max_price:
            max_price = price
        else:
            profit += max_price - price

    print(f"#{i} {profit}")
