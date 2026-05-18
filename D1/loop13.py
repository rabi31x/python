num = int(input())
data = []
while num > 0:
    data.append(num%2)
    num //= 2
print(*data, sep="")
