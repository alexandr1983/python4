def fibo_gen(n):
    k = 1
    for i in range(n + 1):
        yield f"{i}! = {k}"
        k *= i + 1

for el in fibo_gen(int(input("Enter number: "))):
    print(el)
