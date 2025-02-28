# def fib(N):
#     if(N<3):
#         return 1
#     else:
#         return fib(N-1)+fib(N-2)

# print(fib(8))

fib = 0
fibs = 1
fibss = 1
while fib < 10000:
    fib = fibs + fibss
    print(fib)

    fibss = fibs
    fibs = fib
