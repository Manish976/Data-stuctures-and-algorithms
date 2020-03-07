list=[5,15,13,12,16,10]

for i in range(len(list)):
    for j in range(0,i+1):
        # print(j)

        if list[i]<list[j]:
            list[i],list[j]=list[j],list[i]


print(list)
