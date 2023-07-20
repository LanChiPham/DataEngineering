## 4. Dynamic Programming

## Fibonacci sequence: A classic example of a problem that can be solved using dynamic programming is the Fiboncacci sequence.


def fibonacci(n):
    if n <=0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(10))