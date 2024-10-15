def findTop3FrequentNumbers(number_string):
    number_counts = {}
    
    for char in number_string:
        number = int(char) 
        if number in number_counts:
            number_counts[number] += 1 
        else:
            number_counts[number] = 1
    
    sorted_counts = sorted(number_counts.items(), key=lambda item: item[1], reverse=True)

    top_3_counts = sorted_counts[:3]
    
    top_3_sorted = sorted(top_3_counts, key=lambda item: item[0])
    
    top_3_dict = {num: count for num, count in top_3_sorted}
    
    return top_3_dict

number_string_1 = '123456789123455555'
number_string_2 = '1234567890'
number_string_3 = '111111111222222223333333344444444444444444444444444'
print(f"Тест со строкой: {number_string_1}\nРезультат: {findTop3FrequentNumbers(number_string_1)}")
print(f"Тест со строкой: {number_string_2}\nРезультат: {findTop3FrequentNumbers(number_string_2)}")
print(f"Тест со строкой: {number_string_3}\nРезультат: {findTop3FrequentNumbers(number_string_3)}")