one = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
two = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
three = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

def deleteBadMark(arrayMark):
    while 2 in arrayMark:
        arrayMark.remove(2)
    return arrayMark

def replaceBadMark(arrayMark):
    newMarks = (' '.join(str(el) for el in arrayMark))
    newMarks = newMarks.replace('3', '4')
    return [int(x) for x in newMarks.split()]

def helpForBoris(arrayMark):
    arrayMark = deleteBadMark(arrayMark)
    arrayMark = replaceBadMark(arrayMark)
    return arrayMark

print(f"Старые оценки:\n{one}\nНовые оценки:\n{helpForBoris(one)}")
print(f"Старые оценки:\n{two}\nНовые оценки:\n{helpForBoris(two)}")
print(f"Старые оценки:\n{three}\nНовые оценки:\n{helpForBoris(three)}")