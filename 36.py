def fast_pow(a, b):
    result = 1
    x = a
    y = b

    while y > 0:
        if y & 1:
            result *= x
        x *= x
        y >>= 1

    return result

print(fast_pow(2, 9))