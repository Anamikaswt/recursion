def fibonacci(n):
    if n<=1:
        return (n)
    else:
        return(fibonacci(n-1) + fibonacci(n-2))

n = int(input("Enter a number, N, N>=2"))

fibonacci_new = []

for i in range(0,n):
    fibonacci_new.append(fibonacci(i))
    
print(fibonacci_new)