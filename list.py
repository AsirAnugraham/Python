def count(lst):

    even = 0
    odd = 0

    for i in  lst:
        if i%2==0:
            even+=1
        else:
            odd+=1

    return even,odd

lst = [70,17,47,56,45,36,49,89,23]

even , odd = count(lst)

print("Even : {} and Odd : {}".format(even,odd))