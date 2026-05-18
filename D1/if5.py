data = input()
chdata = data.isalpha()
if data.islower() == True:
    chdata = data.upper()
elif data.isupper() == True:
    chdata = data.lower()

print(f"{data}(ASCII: {ord(data)}) => {chdata}(ASCII: {ord(chdata)})")
