def integer_to_roman(integer):
    values = [
        [1000, "M"],
        [900, "CM"],
        [500, "D"],
        [400, "CD"],
        [100, "C"],
        [90, "XC"],
        [50, "L"],
        [40, "XL"],
        [10, "X"],
        [9, "IX"],
        [5, "V"],
        [4, "IV"],
        [1, "I"]
    ]
    roman_string = ''
    while integer > 0:
        for value in values:
            if integer >= value[0]:
               roman_string += value[1]
               integer -= value[0]
               break

    return roman_string

print(integer_to_roman(15))