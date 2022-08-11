def height(root):
    if root is None:
        return 0

    height = 0
    arr = []
    arr.append(root)
    arr.append(None)

    while (len(arr) > 0):
        node = arr[0]
        arr.pop(0)
        if (node is None):
            height += 1
        if (node is not None):
            if (node.left):
                arr.append(node.left)
            if (node.right):
                arr.append(node.right)
        elif (len(arr) > 0):
            arr.append(None)
    return height - 1




