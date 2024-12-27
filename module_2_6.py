
x = int(input("Введите число: "))
y = []
z = str()
for i in range(1,x):
    for j in range(1,x):
        if x % (i + j) == 0 and i!=j:
            if ([i, j]) not in y and ([j, i]) not in y:
                y.append([i,j])
                z += str(i) + str(j)
print(x,z)


"""if ([i,j]) not in y and ([j,i]) not in y:"""
"""and i!=j"""
