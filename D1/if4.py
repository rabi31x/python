a = 1
data = []
for i in range(1, a + 2):
    data.append(input())
if data[0] == "바위":
    if data[1] == "가위":
        print("Result : Man1 Win!")
    elif data[1] == "바위":
        print("Result : Draw")
    elif data[1] == "보":
        print("Result : Man2 Win!")
if data[0] == "가위":
    if data[1] == "보":
        print("Result : Man1 Win!")
    elif data[1] == "가위":
        print("Result : Draw")
    if data[1] == "바위":
        print("Result : Man2 Win!")
if data[0] == "보":
    if data[1] == "바위":
        print("Result : Man1 Win!")
    elif data[1] == "보":
        print("Result : Draw")
    if data[1] == "가위":
        print("Result : Man2 Win!")