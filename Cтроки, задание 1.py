stroke = input('������� ������: ')
stroke.lower()
stroke_reverse = stroke[::-1]
if stroke == stroke_reverse:
    print('yes')
else:
    print('no')

print('��������� ������:', stroke)
print('�������� ������:', stroke_reverse)