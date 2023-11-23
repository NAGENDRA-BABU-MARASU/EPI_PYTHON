def integer_to_spreadsheet_column(integer):
    result = ''
    while integer:
        mod = (integer -1 ) % 26
        result += chr(mod + 65)
        integer = (integer - 1) // 26


    return ''.join(reversed(result))

print(integer_to_spreadsheet_column(27))