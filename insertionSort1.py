def insertionSort1(n, arr):

    for i in range(1, len(arr)):
        num = arr[i]
        j = i - 1
        while j >= 0 and num < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            print(*arr)
        arr[j + 1] = num
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         j = i
#         while j > 0 and arr[j] <= arr[j-1]:
#             arr[j], arr[j-1] = arr[j-1], arr[j]
#             j -= 1
#
#if __name__ == '__main__':
    # n = int(input().strip())
    #
    # arr = list(map(int, input().rstrip().split()))
    # insertion_sort(arr)




