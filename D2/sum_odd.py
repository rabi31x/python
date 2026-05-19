t = int(input())
data = []
result = 0
for case in range(1, t+1):
    data = list(map(int, input().split()))
    result_list = []
    result = 0
    for j in range(len(data)):
        if data[j] % 2 == 1:
            result_list.append(data[j])
    result = sum(result_list)
    print(f"#{case} {result}")

