num = int(input())
count =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
while num > 0:
    count[num%10] += 1
    num //= 10
print(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(*count)
