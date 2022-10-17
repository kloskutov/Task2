# Функция, рисующая равнобедренный треугольник
def triangle(a):
    for i in range(0, a + 1):
        print(' ' * (a - i) + '*' * 2 * i + '*' + ' ' * (a - i), end='\n\n')


# Функция для вычисления декартова расстояния между гистограммами.
def histDistance(hist1, hist2)->float:
    d = 0
    for i in range(len(hist1)):
        d += (hist2[i] - hist1[i]) ** 2
    
    return d ** 0.5


# Функция для записи гистограмм в файл. Необходимо ввести элементы гистрограммы в строку через пробел.
def WriteHist(newfile):
    with open(newfile, 'w') as outfile:
        for _ in range(2):
            str1 = ' '.join(input().split())
            
            outfile.write(str1 + '\n')


# Функция для чтения гистограмм из файла.
def ReadHist(existfile):
    with open(existfile, 'r') as infile:
        list1 = []
        for line in infile:
            line = list(map(int, line.split()))
            list1.append(line)
    return list1
    

#Примеры вызовов функций
# triangle(3)
# triangle(5)

# hist1 = [0, 5, 6, 7]
# hist2 = [6, 3, 2, 1]

# print(histDistance(hist1, hist2))

# WriteHist('D:\\Pythonchik\\Tasks\\Task2\\text.txt')
# print(ReadHist('D:\\Pythonchik\\Tasks\\Task2\\hist1.txt'))