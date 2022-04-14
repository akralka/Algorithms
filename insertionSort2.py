
def insertionSort2(n, arr):
    for i in range(1, len(arr)):
        num = arr[i]
        j = i-1
        while j >= 0 and num < arr[j]:
            arr [j+1] = arr[j]
            j -= 1
        arr[j+1] = num
        print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)





