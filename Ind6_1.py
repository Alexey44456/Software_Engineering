values = input("Введите последовательность чисел, через пробел: ")
print("tuple: ", tuple([ int(x) for x in values.split(" ") ]))
print("list: ", [ int(x) for x in values.split(" ") ])