import  random

a = random.randint(1, 9)
num = 0;
while True:
    num = input()

    if num == "종료":
        break
    
    num = int(num)
    if num == a:
        break
    elif num < a:
        print(f"{num}보다 높습니다!")
    else:
        print(f"{num}보다 낮습니다!")
        


