def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, 'w', encoding='utf-8')
    for i, string in enumerate(strings):
        text_str = str(string)
        byte_num = file.tell()
        file.write(f'{text_str}\n')
        strings_positions[(i + 1, byte_num)] = text_str
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('/Users/macTSF/Desktop/UrbanProject/UrbanProject/module 7/test.txt', info)
for elem in result.items():
    print(elem)
