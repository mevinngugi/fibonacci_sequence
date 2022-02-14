"""
fib function that when you input a number it checks
if the number belongs to the fibonacci sequence or not.
"""


fib_cache = {}
x = int(
    input("Enter the number you want to check if it exist in the Fibonacci sequence: ")
)


def fib(x):
    if (
        x in fib_cache
    ):  # Used memoization to help with the speed of the recursive function.
        return fib_cache[x]

    if x <= 0:
        return 0
    elif x <= 2:
        return 1
    elif x > 2:
        return fib(x - 1) + fib(x - 2)


for x in range(x + 1):  # Start by creating the squence to the Nth term + 1.
    fib_cache[x] = fib(
        x
    )  # Store the result as a key value pair for the corresponding Nth term.


if x in fib_cache.values():  # Check if the target number is in the sequence or not.
    print(x, " is in the sequence ")
else:
    print(x, " is not in the sequence ")
