tpl_1 = '(1, 2, 3), 1)'
tpl_2 = '(1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3)'
tpl_3 = '(2, 4, 6, 6, 4, 2), 9)'

def remove_element(tplForUpdate):
    lst = transformToList(tplForUpdate)
    finderElement = getFinderElement(tplForUpdate)
    if finderElement in lst:
        lst.remove(finderElement)
        return tuple(list(map(int, lst)))
    else:
        return tuple(list(map(int, lst)))

def transformToList(tpl):
    return (tpl.split('),')[0])[1:].split(', ')

def getFinderElement(tpl):
    return str(tpl[-2])

print(f"Первый тест с массивом {tpl_1}, \nрезультат: {remove_element(tpl_1)}\n")
print(f"Второй тест с массивом {tpl_2}, \nрезультат: {remove_element(tpl_2)}\n")
print(f"Третий тест с массивом {tpl_3}, \nрезультат: {remove_element(tpl_3)}")
    