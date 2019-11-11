"""
简单排序算法思路： items = 1,4,2,3,6,8
从0到len(items)-1遍历下标，-1目的是遍历最后一个数自动就位
确定第一个最小的数，遍历从1，len（items），从i+1 开始遍历的原因是，mix_index = i, 不用自己和本身比较大小,是用mix_index 与 J 比较大小

如果改为从大到小
则只需改变if comp(items[min_index], items[j]):
原因是
"""


def select_sort(origin_items, comp=lambda x, y: x < y):
    """简单选择排序"""
    items = origin_items[:]
    for i in range(len(items) - 1):
        # 0123456
        min_index = i
        for j in range(i + 1, len(items)):  # 12345678
            print('j的值', j)
            if comp(items[j], items[min_index]):  # 如果items[j]小就返回Ture
                print(items[j])  # 小值下标变化，按顺序排序
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
        print('items的值', items)
    return items


if __name__ == '__main__':
    print(select_sort([1, 2, 5, 3, 1, 6, 9]))

