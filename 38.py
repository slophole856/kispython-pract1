def fast_mul_gen(y):
    bits = []
    temp = y
    pos = 0
    while temp > 0:
        if temp & 1:
            bits.append(pos)
        temp >>= 1
        pos += 1
    
    print(f"def f(x):")
    
    if y == 0:
        print(f"    return 0")
        return
    
    for i in range(1, max(bits) + 1):
        if i == 1:
            print(f"    x2 = x + x")
        else:
            print(f"    x{2**i} = x{2**(i-1)} + x{2**(i-1)}")
    
    terms = []
    for pos in bits:
        if pos == 0:
            terms.append("x")
        else:
            terms.append(f"x{2**pos}")
    
    print(f"    return {' + '.join(terms)}")

def test():
    test_values = [3, 5, 7, 15, 23, 42]
    for y in test_values:
        print(f"\n# multiply by {y}")
        fast_mul_gen(y)

test()