stroke = input('Введите строку: ')
stroke.lower()
stroke_reverse = stroke[::-1]
if stroke == stroke_reverse:
    print('yes')
else:
    print('no')

print('Начальная строка:', stroke)
print('Конечная строка:', stroke_reverse)