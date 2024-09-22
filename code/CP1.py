num = 1
for i in range(7):
    if num == 6:
        num *= 5
    elif num == 31:
        break
    else:
        num += 1
print(num)