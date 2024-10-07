results = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1, 30.2, 35.7, 16.9,
           27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]

results.sort()

def getThreeBest(results_list):
    return results_list[-3:]

def getThreeWorst(results_list):
    return results_list[:3]

def getAllFromTen(results_list):
    return results_list


print(
    f'Топ-3 лучших результата: {getThreeBest(results)}\n'
    f'Топ-3 худших результата: {getThreeWorst(results)}\n'
    f'Все результаты начиная с 10-ти: {getAllFromTen(results)}'
)