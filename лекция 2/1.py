# Тема 1. Сложные условия для конструкции if-else, которые состоят из 2-ух или более условий.

num1 = input()
num2 = input()
string1 = input()
string2 = input()

# Пример 1. Условие И
# condition1 равняется True (истино), только оба условия num1 == num2 и string1 == string2 истино
condition1 = num1 == num2 and string1 == string2
if (condition1):
    print('Условие И')

# Пример 2. Условие ИЛИ
# condition2 равняется True (истино), если хотя одно из условий num1 == num2 или string1 == string2 истино
condition2 = num1 == num2 or string1 == string2
if (condition2):
    print('Условие ИЛИ')

# Пример 3. 
if (num1 == num2 or string1 == string2):
    print('Условие ИЛИ')
