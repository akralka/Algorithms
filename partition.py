# quicksort partition
def partition(arr):
    right = []
    left = []
    equal = []
    pivot = arr[0]
    for element in arr:
        if element < pivot:
            left.append(element)
        elif element > pivot:
            right.append(element)
        else:
            equal.append(element)
    #   return left + equal + right
    if len(left) != 0:
        left = partition(left)
    if len(right) != 0:
        right = partition(right)
    arr = left + equal + right
    if len(arr) > 1:
        print(*arr)
    return arr


if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(x) for x in input().split()]
    partition(arr)
