from itertools import count, cycle

def func1(n1, n2):
    for i in count(n1):
        if i > n2:
            break
        else:
            print(i)

def func2(a, s):
    j = 0
    k = cycle(a)
    while j < s:
        print(next(k))
        j += 1


func1(n1 = int(input("Enter n1: ")), n2 = int(input("Enter n2>n1: ")))
func2(a = [57, 4, 10], s = int(input("Enter n3: ")))
