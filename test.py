import sys
s = input()
d = 0
for x in s:
    d += 1
    if d == 5 or d == 9:
        print(x)
    if(d > 9): sys.exit()
