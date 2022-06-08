import time

def fib(n):
    if n<=2:
        return 1
    return fib(n-1)+fib(n-2)

start=time.time()
# print(fib(50)) #50==never stop
# print(time.time()-start)


# def fib_2(n,memo:dict=None):
#     if n in memo:
#         memo[n]=0
#         return memo[n]
#
#     if n<=2:
#         return 1
#     memo[n]=fib(n-1,memo)+fib(n-2,memo)
#     return memo[n]
#
# starta=time.time()
# print(fib_2(50)) #50==never stop
# print(time.time()-starta)


def sum(n):
    return (n*(n+1))/2


# starta=time.time()
# print(sum(500000000000000000))
# print(time.time()-starta)




# starta=time.time()
# print(sum(500000000000000000))
# print(time.time()-starta)

import numpy as np

a=np.arange(1,1000)
print(a[1])
