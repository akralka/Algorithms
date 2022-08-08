# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         j = i
#         while j > 0 and arr[j] <= arr[j-1]:
#             arr[j], arr[j-1] = arr[j-1], arr[j]
#             j -= 1
#     print(arr)

# if __name__ == '__main__':
#     n = int(input().strip())

#     arr = list(map(int, input().rstrip().split()))
#     insertion_sort(arr)
    
--------------------------------------------------------------------------------------------------
def insertionSort2(n, arr):
    for i in range(1, len(arr)):
        num = arr[i]
        j = i-1
        while j >= 0 and num < arr[j]:
            arr [j+1] = arr[j]
            j -= 1
        arr[j+1] = num
        print(*arr) #  Each step

if __name__ == '__main__':
    n = int(input().strip())  # how many numbers in array

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)




