def fast_mul(a, b):
    result = 0
    x = a
    y = b

    while y > 0:
        if y & 1:
            result += x
        x <<= 1
        y >>= 1

    return result

print(fast_mul(10, 9))