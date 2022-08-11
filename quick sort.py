def partition(arr, low, high):
	i = (low-1)
	pivot = arr[high]

	for j in range(low, high):
		if arr[j] <= pivot:
			i +=1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i+1], arr[high] = arr[high], arr[i+1]
	print(*arr)
	return (i+1)


def quickSort(arr, low, high):
	if len(arr) == 1:
		return arr
	if low < high:
		a = partition(arr, low, high)
		quickSort(arr, low, a-1)
		quickSort(arr, a+1, high)

if __name__ == '__main__':
	n = int(input().strip())
	arr = list(map(int, input().rstrip().split()))
	quickSort(arr, 0, n - 1)




