with open ("input.txt_day_2.txt") as file:
    accumulator = 0
    result = 0
    aux = 0
    while accumulator < 100:
        blue_max = 0
        red_max = 0
        green_max = 0
        string = file.readline().split(";")
        for i in string:
            if "blue" in i:
                aux = int(i[i.find("blue") - 3:i.find("blue") - 1].strip())
                if aux  > blue_max:
                    blue_max= aux
            if "red" in i:
                aux = int(i[i.find("red") - 3:i.find("red") - 1].strip())
                if aux > red_max:
                    red_max = aux
            if "green" in i:
                aux = int(i[i.find("green") - 3:i.find("green") - 1].strip())
                if aux > green_max:
                    green_max = aux
        power_set = (green_max * blue_max * red_max)
        result +=power_set
        accumulator+=1
print(result)
                
               
    
