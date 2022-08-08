def output(arr):
    for j in range(len(arr)):
        print(arr[j], end=" ")
        print()

def mergeSort(arr):
    if len(arr) > 1:

        mid = len(arr)//2

        left = arr[:mid]  #from index 0 (default) to mid!
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while j < len(right):    # if sth left in array!
            arr[k] = right[j]
            j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    print("Given array: ")
    output(arr)
    mergeSort(arr)
    print("Sorted array: ")
    output(arr)

# -------------------------------------------------------------------------------------------
# def output(arr):
#     for j in range(len(arr)):
#         print(arr[j], end=" ")
#         print()
# 
# 
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return
# 
#     middle = int(len(arr) / 2)
#     l, r = arr[:middle], arr[middle:]
# 
#     merge_sort(l)
#     merge_sort(r)
# 
#     i = j = k = 0
#     while i < len(l) and j < len(r):
#         if l[i] < r[j]:
#             arr[k] = l[i]
#             i, k = i + 1, k + 1
#         else:
#             arr[k] = r[j]
#             j, k = j + 1, k + 1
# 
#     while i < len(l):
#         arr[k] = l[i]
#         i, k = i + 1, k + 1
#     while j < len(r):
#         arr[k] = r[j]
#         j, k = j + 1, k + 1
# 
# 
# if __name__ == '__main__':
#     arr = list(map(int, input().rstrip().split()))
# 
#     merge_sort(arr)
#     print("Sorted array: ")
#     output(arr)
