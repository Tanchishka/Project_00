def maximum(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    print("max =" ,max_num)

def minimum(numbers):
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    print("min =", min_num)


list_num = [4,6,2,1,9,63,-134,566]
maximum(list_num)
minimum(list_num)

