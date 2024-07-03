import random


def sumoProduct(l1, l2):
    prods = []
    sum = 0
    
    while l1 and l2:
        prods.append(l1[0]*l2[0])
        
        del l1[0]
        del l2[0]
        
    for i in range(len(prods)):
        sum += prods[i]
        
    return sum


numbers1 = [5, 3, 1, 1, 2]
numbers2 = [1, 2, 2, 9, 5]
result = sumoProduct(numbers1, numbers2)
print('Your result : ', result)


numbers1 = [random.randint(1, 10) for i in range(5)]
numbers2 = [random.randint(1, 10) for i in range(5)]
print('numbers 1 ', numbers1)
print('numbers 2 ', numbers2)
result = sumoProduct(numbers1, numbers2)
print('Your result : ', result)

##
