def fibonacci_series(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        series = [0, 1]
        while len(series) < n:
            next_term = series[-1] + series[-2]
            series.append(next_term)
        return series

terms = int(input("Enter the number of terms: "))
result = fibonacci_series(terms)
print("Fibonacci Series:", result)