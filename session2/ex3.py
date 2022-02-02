
def fib(n):
    n1 = 0
    n2 = 1
    if n == 1:
        return n1
    if n == 2:
        return n2
    else:
        for i in range(2, n + 1):
            num = n1 + n2
            n1 = n2
            n2 = num
        return num
def fibosum(num):

