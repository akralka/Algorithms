def left(index):
    return 2*index+1 #left son


def right(index):
    return 2*index+2


def heapify(a, size, index):
    max = index
    l = left(index)
    r = right(index)

    if l < size and a[l] > a[max]:
        max = l

    if r < size and a[r] > a[max]:
        max = r

    if max != index: # if not root, not max
        a[index], a[max] = a[max], a[index]
        heapify(a, size, max)


def heap_sort(arr):
    for i in range(int(len(arr)/2), -1, -1): # from last to 0
        heapify(arr, len(arr), i)

    for i in range(len(arr)-1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]   # max element with index 0
        heapify(arr, i, 0) # "i" size >> max 


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    heap_sort(arr)
    print (arr)


# B = [1,3,1,2,7,9,1,6,1,0,4,2]
# C =[15,3,99,1,25,7,9,9,1,100,6,1,0,12,4,2,9,0,87,122,54]
# D = [0,12,4,2,9,0,87,122,54,1,2,11,55,99]
