def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

fib_numbers = list(fib(200))

with open("fib.txt", "w") as file:
    for number in fib_numbers:
        file.write(f"{number}\n")
    print('Готово')