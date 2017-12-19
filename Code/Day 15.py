def generator(a_start, b_start, a_factor, b_factor, mod, reps):
    pairs = 0
    a_val = a_start
    b_val = b_start
    for i in range(reps):
        a_val = (a_val * a_factor) % mod
        b_val = (b_val * b_factor) % mod
        a_bin = bin(a_val)
        b_bin = bin(b_val)
        if a_bin[-16:] == b_bin[-16:]:
            pairs += 1
    return pairs

# print(generator(65, 8921, 16807, 48271, 2147483647, 40000000))
# print(generator(783, 325, 16807, 48271, 2147483647, 40000000))

def second_generator(a_start, b_start, a_factor, b_factor, mod, reps):
    pairs = 0
    a_val = a_start
    b_val = b_start
    for i in range(reps):
        while a_val % 4 != 0:
            a_val = (a_val * a_factor) % mod
        while b_val % 8 != 0:
            b_val = (b_val * b_factor) % mod
        a_bin = bin(a_val)
        b_bin = bin(b_val)
        if a_bin[-16:] == b_bin[-16:]:
            pairs += 1
        a_val = (a_val * a_factor) % mod
        b_val = (b_val * b_factor) % mod
    return pairs

# print(second_generator(65, 8921, 16807, 48271, 2147483647, 5000000))
print(second_generator(783, 325, 16807, 48271, 2147483647, 5000000))