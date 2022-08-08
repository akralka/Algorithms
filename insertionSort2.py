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




