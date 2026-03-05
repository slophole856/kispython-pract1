def mul_bits(x, y, bits):
    x &= (2 ** bits - 1)
    y &= (2 ** bits - 1)
    return x * y

def mul16(x, y):
    x_lo = x & 0xFF
    x_hi = x >> 8
    y_lo = y & 0xFF
    y_hi = y >> 8

    p0 = mul_bits(x_lo, y_lo, 8)
    p1 = mul_bits(x_lo, y_hi, 8)
    p2 = mul_bits(x_hi, y_lo, 8)
    p3 = mul_bits(x_hi, y_hi, 8)

    return p0 + ((p1 + p2) << 8) + (p3 << 16)

print(mul16(10, 4))