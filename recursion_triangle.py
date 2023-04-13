def print_triangle(base):
    if base == 0:
        return
    else:
        for x in range(base):
            print("*", end="")
        print()
        print_triangle(base - 1)

def main():
    base = 5
    print(print_triangle(base))

if __name__ == "__main__":
    main()