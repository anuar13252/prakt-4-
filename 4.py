import math


def input_array(row, column):
    array = []
    for i in range(0, row):
        sub_array = []
        for j in range(column):
            if j == 0:
                print('Введите число [ ', i, ' ]', '[ ', j, ' ]:')
                number = int(input())
                sub_array.append(number)
            if j == 1:
                sub_array.append(0)
        array.append(sub_array)
    return array


def output_array(array):
    print()
    for i in array:
        for j in i:
            print("%d\t" % j, end='')
        print('')


def main():
    array = input_array()
    output_array(array)

    for i in range(0, 10):
        if array[i][0]>=0:
            proiz=1
            summa=0
            for j in range(i):
                if array[j][0] % 2 == 0:
                    summa += array[j][0]
                    proiz *= array[j][0]
                else:
                    proiz *= array[j][0]
            answer=proiz-summa
        else:
            summa=0




    output_array(array)



if __name__ == '__main__':
    main()