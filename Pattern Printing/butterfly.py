n=5
for i in range(n):
        print("*" * (i + 1) + " " * (2 * (n - i - 1)) + "*" * (i + 1))

for i in range(n - 1, -1, -1):
     print("*" * (i + 1) + " " * (2 * (n - i - 1)) + "*" * (i + 1))