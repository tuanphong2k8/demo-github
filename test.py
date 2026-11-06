import math
a, b, c = map(int, input().split())
if(a + b <= c or b + c <= a or c + a <= b):
    print("Khong phai 3 canh cua tam giac")
else:
    p = (a + b + c)/2
    res = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(f"{res:.1f}")