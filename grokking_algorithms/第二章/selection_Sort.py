# -*- coding:utf-8 -*-


# 寻找最小
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(0, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)  # 将list 中最小元素找出来，添加删除，然后重复执行
        newArr.append(arr.pop(smallest))
        print(newArr)
    return newArr


if __name__ == '__main__':
    print(selectionSort([11,4,2,145,1,2,4]))


