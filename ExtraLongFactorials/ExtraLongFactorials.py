def extraLongFactorials(n):
    fact = 1
    if n < 3:
        print(1)
    else:
        for i in range(2,n+1):
            fact = fact*i
        print (fact)

n = int(input())
extraLongFactorials(n)
