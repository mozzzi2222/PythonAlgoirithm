
def gcd(a, b):

    r = a % b
    if a % b == 0:
        print(b)
        return 0
    gcd(b, r)

gcd(192, 162)