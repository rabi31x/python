data = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
sum = 0
i= 0;
while i < len(data):
    if int(data[i]) >= 80:
        sum += int(data.pop(i))
    else:
        i += 1
print (sum)

    