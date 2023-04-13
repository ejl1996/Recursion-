def factorial(value):
    # Base case: if n is 0 or 1, return 1
    if value == 0 or value == 1:
        return 1

    # Recursive case: if n is greater than 1, call the function with n-1 and multiply by n
    else:
        return value * factorial(value - 1)

def main():
    result = factorial(5)
    print(result)  # Output: 120

if __name__ == "__main__":
    main()
