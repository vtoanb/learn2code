# Python execute fibonaci compare with node.js

import time

def fibonaci(n):
    if(n == 0): return 0
    elif(n == 1): return 1
    return fibonaci(n-1) + fibonaci(n-2)

if __name__ == '__main__':
    t1 = time.time()
    print(fibonaci(35))
    t2 = time.time()
    print(t2-t1)
