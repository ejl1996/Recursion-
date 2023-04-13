def print_numbers(bound):
    if bound == 0:
        print(0)
    else:
        print(bound)
        print_numbers(bound - 1)

def main():
    bound = 5
    print(print_numbers(bound))

if __name__ == "__main__":
    main()