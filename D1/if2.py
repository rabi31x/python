a = int(input())
list = []
for i in range(1, a + 1):
    if a%i ==0:
        print(f"{i}(은)는 {a}의 약수입니다.")
        list.append(i)

if len(list) == 2:
    print(f"{a}(은)는 {list[0]}과 {list[1]}로만 나눌 수 있는 소수입니다.")
