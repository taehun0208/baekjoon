import math
def solution(numer1, denom1, numer2, denom2):
    top = (numer1*denom2) + (numer2*denom1)
    bottom = (denom1*denom2)
    gcd = math.gcd(top,bottom)
    return [top//gcd, bottom//gcd]