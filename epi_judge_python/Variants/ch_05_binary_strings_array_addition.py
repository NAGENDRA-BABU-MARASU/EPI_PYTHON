def binary_addition_strings(arr1, arr2):
    min_length = min(len(arr1), len(arr2))
    new_string = [0 for i in range(min_length)]
    carry_out = 0
    for i in reversed(range(min_length)):
        current_char = arr1[i] + arr2[i] + carry_out
        if current_char > 1:
            new_string[i] = 0
            carry_out = 1
        else:
            new_string[i] = current_char
            carry_out = 0
    if carry_out:
        new_string.insert(0, 1)
    return new_string

print(binary_addition_strings([1,0,0,1], [1,0,1,1]))