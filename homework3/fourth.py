def stepen(a,b):
    if a > b:
        result = 1
        for _ in range(abs(b)):
            result *= 1 / a
        print(result)

stepen(14,-2)