array1=[3,1,4,7]
array2=[6,8,5,9]
array=array1+array2
i=0
while i< len(array):
    a=i
    j=i+1
    while j<len(array):
        if array[a]>array[j]:
            a=j
        j=j+1
    array[i],array[a]=array[a],array[i]
    i+=1
print(array)