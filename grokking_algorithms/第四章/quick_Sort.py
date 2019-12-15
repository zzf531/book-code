# -*- coding:utf-8 -*-
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        print('小鱼基准值', less)
        greater = [i for i in array[1:] if i > pivot]
        print('大于基准值', greater)
        return quicksort(less) + [pivot]


print(quicksort([10, 5, 2, 3, 15, 19, 21]))
