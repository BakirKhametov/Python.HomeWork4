# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

def listofnonrepeatingelements(change_list):
    change_list = []
    for i in original_list:
        if i not in change_list:
            change_list.append(i)
    print(f"Список из неповторяющихся элементов: {change_list}")


original_list = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Оргинальный список: {original_list}")
listofnonrepeatingelements(change_list=True)


