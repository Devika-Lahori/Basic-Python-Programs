list1=[]
for i in range(1,11):
    list1.append(i)
print("Original List:",list1)
list2=list1[0:5]
print("Extracted first five elements:",list2)
list2.reverse()
print("Reversed extracted elements:",list2)