# Recursion makes reference to call the same function inside the function

# They have 2 elements
# base case / determines the case that interrupt the recursion
# recursive case / the smaller version

# Sample: Fibonacci series fib(n) = fib(n-1) + fib(n-2)

# returns the number in the position specified by n
# zero indexed
def fibonacci(n):
    print(f"==== n is -> {n} =====")
    if n == 0 or n == 1:
        return n
    else:
        print(f"=== result -> {fibonacci(n - 1) + fibonacci(n - 2)}")
        return fibonacci(n - 1) + fibonacci(n - 2)


result = fibonacci(4)
print(result)
