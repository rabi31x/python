data = []
for i in range(1, 101):
    if i % 2 != 0:
        data.append(str(i))
print(", ".join(data))