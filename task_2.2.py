def quarter_m(month):
    if month in range(1, 4):
        month = 1
    elif month in range(4, 7):
        month = 2
    elif month in range(7, 10):
        month = 3
    else:
        month = 4
    print(month)

num_month = int(input())
quarter_m(num_month)
