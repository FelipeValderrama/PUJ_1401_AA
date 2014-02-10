lines = int(input())
while lines != 0:
    lines -= 1
    c, w, dw = [int(x) for x in input().split()]
    valid = 'yes' if c * dw <= w else "no"
    print(valid)
