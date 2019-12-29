"""
52、list=[2,3,5,4,9,6]，从小到大排序，不许用sort，输出[2,3,4,5,6,9]
利用min()方法求出最小值，原列表删除最小值，新列表加入最小值，递归调用获取最小值的函数，反复操作
"""
origin_list = [2, 3, 5, 4, 9, 6]
min_list = []


def get_min(new_list):
    a = min(new_list)
    min_list.append(a)
    new_list.remove(a)
    if len(new_list) > 0:
        get_min(new_list)
    return min_list

print(get_min(origin_list))


