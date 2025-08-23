import math


t = 0

a = 125
b = 62.5

for t in range (5,35,5):
    x = float(input(f"enter 'x' for {t} minutes : "))
    d = a-x
    D  = b -x
    g = b*d
    f = a*D
    l = math.log10(g/f)
    k = (2.303/(t*b)) * l
    

    print(f"(a-x) for {t} minutes is :{d}")
    print(f"(b-x) for {t} minutes is :{D}")
    print(f"log b(a-x)/a(b-x) for {t} minutes is :{l}")
    print(f"'K' for {t} minutes is :{k}")




    



    