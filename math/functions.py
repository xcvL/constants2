def agm(a, b, tol=1e-12):
    while abs(a - b) > tol:
        a_next = (a + b) / 2
        b_next = (a * b) ** 0.5
        a, b = a_next, b_next
    return a