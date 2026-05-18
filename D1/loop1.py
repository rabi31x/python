data =[88, 30, 61, 55, 95]
for i in range (1, 6):
    if data[i-1] >= 60:
        print(f"{i}번 학생은 {data[i-1]}점으로 합격입니다.")
    else:
        print(f"{i}번 학생은 {data[i-1]}점으로 불합격입니다.")
