def seq(items, key):
    for index, item in enumerate(items):
        if item == key:
            return index
    return -1


print(seq([1,2,3,4,5,3],3))


def bin_sarch(items, key):
    start, end = 0, len(items) - 1
    items.sort()
    while start <= end:
        min = (start+end) // 2
        if key > items[min]:
            start = min + 1
        elif key < items[min]:
            end = min - 1
        else:
            return min
    return -1

print(bin_sarch([1,3,4,5,6,1,2,3,4,5,6], 4))


# t = enumerate([1,2,3,4,5])
# for i in t:
#     print(i)tt.py:27
# try:
#     print([1,2,3,4,5,4].index(41))
# except ValueError:
#     print(-1)

def is_leap_year(year):
    return  (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
for i in range(1,6):
    print(i * "*")