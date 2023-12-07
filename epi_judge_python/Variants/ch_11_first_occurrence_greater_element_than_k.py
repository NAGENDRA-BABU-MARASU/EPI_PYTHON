def search_next_first_greater_key(A, key):
    left, right = 0 , len(A) -1
    result = -1
    while left <= right:
        mid = left + (right - left) // 2
        if A[mid] == key:
            left = mid + 1
            result = mid
        elif key > A[mid]:
            left = mid + 1
        else:
            result = mid
            right = mid - 1

    return result

print(search_next_first_greater_key([-14,-10,2,108,108,243,285,285,285,401], 108))