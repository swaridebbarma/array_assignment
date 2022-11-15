a=[2,6,7,5,6,7,7,1,8]
new_a=[]
for i in a:
    if i not in new_a:
        new_a.append(i)
print(new_a)