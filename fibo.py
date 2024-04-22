def recursive_nth_fibo(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return recursive_nth_fibo(n-1) + recursive_nth_fibo(n-2)


def main():
    try:
        n = int(input("Enter the number of Fibonacci sequence elements: "))
        fibo_sequence = [recursive_nth_fibo(i) for i in range(1, n+1)]
        print("Fibonacci sequence:", fibo_sequence)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
