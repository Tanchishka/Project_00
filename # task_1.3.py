# task_1.3.py

test_number = int(input("Число месяца 2023г. :",))

month31 = [1, 3, 5, 7, 8, 10, 11]
month30 = [4, 6, 9, 12]
month28 = [2]
if test_number in month31:
  print("Колличество дней в месяце: 31")

elif test_number in month28:
  print("Колличество дней в месяце:28")

elif test_number in month30:
  print("Колличество дней в месяце: 30")
else:
  print("Месяца по таким номером не существует")
