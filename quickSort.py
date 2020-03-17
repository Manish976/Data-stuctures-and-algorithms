def partition(sort_list, low, high):
    i = (low - 1)
    pivot = sort_list[high]
    for j in range(low, high):
        if sort_list[j] <= pivot:
            i += 1
            sort_list[i], sort_list[j] = sort_list[j], sort_list[i]
    sort_list[i + 1], sort_list[high] = sort_list[high], sort_list[i + 1]
    return (i + 1)


def quick_sort(sort_list, low, high):
    if low < high:
        pi = partition(sort_list, low, high)
        quick_sort(sort_list, low, pi - 1)
        quick_sort(sort_list, pi + 1, high)


lst = [29,99,27,41,66,28,44,78]

low = 0
high = len(lst) - 1
quick_sort(lst, low, high)
print(lst)