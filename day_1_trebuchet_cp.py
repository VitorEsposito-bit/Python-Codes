with open('input.txt', 'r') as file:
    lista = ["1","2","3","4","5","6","7","8","9"]
    accumulator = 0
    while True:
        number= ""
        for element in file.readline():
            if element in lista:
                number+=element
        if number == "":
            break
        number = number[0] + number[-1]
        accumulator+=int(number)
print(accumulator)

