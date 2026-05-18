data = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
an, bn, on, abn = 0, 0, 0, 0
for i in data:
    if i == 'A':
        an += 1
    elif i == 'B':
        bn += 1
    elif i == 'O':
        on += 1
    else:
        abn += 1
print(f"{{'A': {an}, 'O': {on}, 'B': {bn}, 'AB': {abn}}}")

    
