def multiply_by_15(x):
    a = x + x
    b = a + a 
    c = b + b
    d = c - x

    result = c + d
    
    return result

print(multiply_by_15(10))