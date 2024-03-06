from collections import defaultdict

def default_value_one():
    return 1

with open ("input_day_4.txt") as file:
    cards_data = defaultdict(default_value_one)
    for x in range(1,205,1):
        cards_data[x]
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
        for y in range(cards_data[i]):
            aux_2 = i + 1
            for j in range(accumulator):
                cards_data[aux_2]+=1
                aux_2+=1
        result+=cards_data[i]
        i+=1
print(result)
