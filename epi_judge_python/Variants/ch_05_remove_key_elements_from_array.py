def remove_key_elements_from_array(A, key):
    writing_index = 0
    count = 0
    for i in range(0, len(A)):
        if A[i] != key:
            A[writing_index] = A[i]
            writing_index += 1

    return len(A[:writing_index])

print(remove_key_elements_from_array([1,3,2,3,3,3,4,5,6,3], 3))