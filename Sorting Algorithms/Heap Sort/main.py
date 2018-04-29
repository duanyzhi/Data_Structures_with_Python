def heap_sort(lst):
    for start in range(int((len(lst) - 2) / 2), -1, -1):
        siftdown(lst, start, len(lst) - 1)
    for end in range(len(lst) - 1, 0, -1):
        lst[end], lst[0] = lst[0], lst[end]
        siftdown(lst, 0, end - 1)
    return lst


def siftdown(lst, start, end):
    root = start
    while True:
        child = 2 * root + 1
        if child > end: break
        if child + 1 <= end and lst[child] < lst[child + 1]:
            child += 1
        if lst[child] > lst[root]:
            lst[child], lst[root] = lst[root], lst[child]
            root = child
        else:
            break

arr = [3, 4, 1, 8, 2, 9, 6, 5, 7, 10]
print(heap_sort(arr))
