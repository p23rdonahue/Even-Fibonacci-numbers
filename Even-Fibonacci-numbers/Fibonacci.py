fib = []
a, b = 0, 1
for i in range(1,40):
    a, b = b , a + b
    if b % 2 == 0 and b < 4000000:
        fib.append(b)
print("sum", fib)
print("Answer", sum(fib))
