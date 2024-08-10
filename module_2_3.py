print(f"{"Задача"} {'"Нули ничто, отрицание недопустимо!"'}")
#
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
numbers = my_list[0]
while index < len(my_list):
    if numbers > 0:
        print(numbers)
        numbers = my_list[index + 1]
        index += 1
    elif numbers == 0:
        numbers = my_list[index + 1]
        index += 1
        continue
    else:
        break
