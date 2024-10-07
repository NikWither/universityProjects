one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

def giveMaxSide(array):
    return max(array)

def giveMinSide(array):
    return min(array)

def findTrinagleArea(a, b, c):
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c))**0.5
    return s

aMax, bMax, cMax = giveMaxSide(one), giveMaxSide(two), giveMaxSide(three)
print("Максимальная площадь треугольника - ", findTrinagleArea(aMax, bMax, cMax))

aMin, bMin, cMin = giveMinSide(one), giveMinSide(two), giveMinSide(three)
print("Минимальная площадь треугольника - ", findTrinagleArea(aMin, bMin, cMin))
