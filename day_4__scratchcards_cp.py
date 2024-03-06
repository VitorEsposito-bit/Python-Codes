with open ("input_day_4.txt") as file:
    i = 1
    result = 0
    while i != 205:
        points = 0
        accumulator = 0
        teste = file.readline().strip().split("|")
        aux = teste[0].split(":")
        winning_numbers = aux[1].strip(" ").replace("  "," ").split(" ")
        your_numbers = teste[1].strip(" ").replace("  "," ").split(" ")
        for x in your_numbers:
            if x in winning_numbers:
                accumulator+=1
        for y in range(accumulator):
            if y ==0:
                points+=1
            else:
                points*=2
        result+=points
        i+=1
    print(result)
        