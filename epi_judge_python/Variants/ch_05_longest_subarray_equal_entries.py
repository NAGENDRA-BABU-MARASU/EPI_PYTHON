def longest_subarray_equal_entries(A):
    longest_length = 1
    current_length = 1
    for i in range(1, len(A)):
        if A[i] == A[i-1]:
            current_length += 1
            longest_length = max(current_length, longest_length)
        else:
            current_length = 1

    return longest_length

print(longest_subarray_equal_entries([1,1,1,2,2,2,2,2,3,3,3,3,3,3,3,3,4,6,7]))
