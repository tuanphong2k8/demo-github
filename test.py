c = input()
k = ord(c)
if k >= 65 and k <= 90:
    print(chr(k + 32))
else :
    print(chr(k - 32))