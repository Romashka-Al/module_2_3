asd = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
while a < len(asd):
    if asd[a] > 0:
        print(asd[a])
    if asd[a] < 0:
        break
    a += 1
