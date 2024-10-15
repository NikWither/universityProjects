def transformToList(tpl):
    return (tpl.split('),')[0])[1:].split(', ')

def getFinderElement(tpl):
    return str(tpl[-2])

def findEmployer(tplForUpdate):
    lst = transformToList(tplForUpdate)
    finderElement = getFinderElement(tplForUpdate)
    if lst.count(finderElement) == 0:
        return ()
    if lst.count(finderElement) == 1:
        newArray = lst[lst.index(finderElement):]
        return tuple(list(map(int, newArray)))
    else:
        count = 0
        startAndEndEmployer = ''
        for i in range(len(lst)):
            if lst[i] == finderElement and count != 2:
                count += 1
                startAndEndEmployer += str(i)
        startJob = int(startAndEndEmployer[0])
        endJob = int(startAndEndEmployer[1])
        newArray = lst[startJob:endJob + 1]
        return tuple(list(map(int, newArray)))
    
tpl_1 = '(1, 2, 3), 8)'
tpl_2 = '(1, 8, 3, 4, 8, 8, 9, 2), 8)'
tpl_3 = '(1, 2, 8, 5, 1, 2, 9), 8)'
        
print(f"\nРезультат: {findEmployer(tpl_1)}")
print(f"\nРезультат: {findEmployer(tpl_2)}")
print(f"\nРезультат: {findEmployer(tpl_3)}")