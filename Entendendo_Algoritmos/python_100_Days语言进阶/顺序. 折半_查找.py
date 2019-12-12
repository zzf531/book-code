def ben_seach(items, key):
    start, end = 0, len(items) - 1
    while end > start:
        mid = (start + end) // 2
        if key > items[mid]:
            start = mid +1
        elif key < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1


print(ben_seach([1,2,3,4,5,6,7,9], 4))
