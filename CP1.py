def count_words(filename):

    most_common_word = 0
    max_count = 0

    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read().lower()

    words = text.split()

    word_count = {}
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for word, count in word_count.items():
        if count > max_count:
            max_count = count
            most_common_word = word
    
    print(f'Количество слов: {len(words)}')
    print(f'Самое часто встречающееся слово: "{most_common_word}", встречается {max_count} раз')

if __name__ == '__main__':
    count_words('DigitalRuble')
