text = input('Enter the text your text: ')
vowels = 0
checkThe = 'Предложение не начинается на "The"'
checkEnd = 'не заканчивается на "end"'
length = len(text) # подсчет количества символов
text = text.lower() # перевод в нижний регистр
# подсчет количество гласных a, e, i, o, u
for i in range(length):
    if text[i] == 'a' or text[i] == 'e' or text[i] == 'i' or text[i] == 'o' or text[i] == 'u':
        vowels += 1
text.replace(' ugly', ' beauty') # замена ugly на beauty
# проверки на начало the и конец end
if text[:3] == 'the':
    checkThe = 'Предложение начинается на "The"'
if text[-4:] == ' end' or text[-5:] == ' end.':
    checkEnd = 'заканчивается на "end"'

print(f'{text}\nДлина предложения - {length}\nГласных "a, e, i, o, u" в тексте - {vowels}\n{checkThe} и {checkEnd}.')