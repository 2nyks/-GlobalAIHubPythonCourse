list = [1,2,3,4,5,6]
i=0
l=len(list)
for i in range(l // 2):
    list[i], list[l // 2 + i] = list[l // 2 + i], list[i]
print(list)


