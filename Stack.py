list=[10,29,93,27,26,16,48]
print("The List is :",list)
for i in range(len(list)):
    print("the popped item is ",list.pop(-1))
    print(list)
    print(end='\n')