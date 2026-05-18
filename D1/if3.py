num = int(input())
list = []
for i in range(1, num + 1):
    list.append(input())
for i in range(1, num + 1):
    if list[i-1].islower():
        print(f"#{i} {list[i-1]} 는 소문자 입니다.")
    else:
        print(f"#{i} {list[i-1]} 는 대문자 입니다.")

