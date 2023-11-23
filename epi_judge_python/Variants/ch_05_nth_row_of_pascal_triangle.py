def generate_nth_row_of_pascal_traingle(n):
    previous_row = [1,1]
    current_row = []
    for i in range(2,n):
        for j in range(i+1):
            if j == 0 or j == i:
                current_row.append(1)
            else:
                current_row.append(previous_row[j-1] + previous_row[j])

        previous_row = current_row
        current_row = []

    return previous_row

print(generate_nth_row_of_pascal_traingle(3))


