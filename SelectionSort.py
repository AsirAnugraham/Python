def sort(list):

    for i in range(len(list)-1):
        minpos = i
        for j in range(i,len(list)):
             if list[j] < list[minpos]:
                 minpos = j

        temp = list[i]
        list[i] = list[minpos]
        list[minpos] = temp
        print(list)


list = [4,2,5,7,1,9]
sort(list)
print(list)