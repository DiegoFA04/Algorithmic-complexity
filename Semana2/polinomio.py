def solve(x0, a: list):
    res = 0.0
    for i, ai in enumerate(reversed(a)):
        res += ai * x0 ** i		# ** es potencia
    return res

result = solve(2, [10, 20, 0, 15, 5, 50])

print(result)
