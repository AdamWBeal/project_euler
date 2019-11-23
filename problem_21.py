def sum_of_divisors(x):
    value = 0
    for i in range(1,int((x/2)+1)):
        if x % i == 0:
            value += i
    return value

def is_prime(x):
    return True if x in [2,3] else not any (x % n == 0 for n in range (2, int (x ** 0.5) + 1))

def amicable(n):
    total = 0
    a = []
    b = []
    for num in range(1, n+1):
        if not is_prime(num):
            a.append(num)

    for num in a:
        val = sum_of_divisors(num)
        if sum_of_divisors(val) == num and val != num:
            pair = [val,num]
            pair.sort()
            if pair not in b:
                b.append(pair)
    for i in b:
        total += (i[0]+i[1])

    return total

x = amicable(10000)
print(x)
