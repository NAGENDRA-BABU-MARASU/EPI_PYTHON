def right_propogate_rightmost_set_bit(x):
    return (x | x-1)

print(bin(right_propogate_rightmost_set_bit(0b01010000)))