

def calc(line):
    
    operand_1, operation, operand_2 = line.split(' ')
    operand_1 = int (operand_1)
    operand_2 = int (operand_2)
    
    # if operation == '+':
    #     print(f' Результат:{(operand_1) + operand_2} ')
    # if operation == '-':
    #     print(f' Результат:{operand_1 - operand_2} ')
    # if operation == '/':
    #     print(f' Результат:{operand_1 / operand_2} ')
    # if operation == '//':
    #     print(f' Результат:{operand_1 // operand_2} ')
    # if operation == '%':
    #     print(f' Результат:{operand_1 % operand_2} ')
    # if operation == '*':
    #     print(f' Результат:{operand_1 * operand_2} ')

count = 0

with open('data.txt', 'r') as file:
    for line in file:
        try: 
            count += 1
            calc(line)
            
        except ValueError as exp:
            if 'unpack' in exp.args[0]:
                print(f"Ошибка в линии {count}, не хватает данных для ответа")
            else:
                print(f'ошибка в линии {count}, нельзя перевести в число')
   