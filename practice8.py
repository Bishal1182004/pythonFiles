def print_pattern(n):
    for i in range(1, n + 1):
        for j in range(n, 0, -1):
            # Print current number i times
            for _ in range(i):
                print(j, end=" ")
        print(-1, end=" ")
    print(-1)

# Test the pattern
if __name__ == "__main__":
    n = int(input("Enter n: "))
    print_pattern(n)
