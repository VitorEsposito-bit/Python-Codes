with open('input.txt_day_2.txt','r') as file:
    accumulator = 0
    result = 0
    while accumulator < 100:
        string = file.readline().split(";")
        for i in range(len(string)):
            blue = 0
            red = 0
            green = 0
            if "blue" in string[i]:
                try:
                    blue+=int(string[i][string[i].find("blue") - 3:string[i].find("blue")-1])
                except:
                    blue+=int(string[i][string[i].find("blue") - 2])
            if "red" in string[i]:
                try:
                    red+=int(string[i][string[i].find("red") - 3:string[i].find("red")-1])
                except:
                    red+=int(string[i][string[i].find("red") - 2])
            if "green" in string[i]:
                try:
                    green+=int(string[i][string[i].find("green") - 3:string[i].find("green") - 1])
                except:
                    green+=int(string[i][string[i].find("green") - 2])
            if red > 12 or green > 13 or blue > 14:
                break
            if i == (len(string) - 1):
                try:
                    aux = int(string[0][5:7])
                    result+=aux
                except:
                    aux = int(string[0][5])
                    result+=aux
        accumulator+=1
print(result)




    

