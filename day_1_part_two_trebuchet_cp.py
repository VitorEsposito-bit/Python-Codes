with open("input.txt", "r") as file:
    data = [x.strip() for x in file.readlines()]

    def find_string(string,dict):
        for key in dict:
            if key in string:
                return key
            
    dict = {"one":"1",
            "two":"2",
            "three":"3",
            "four":"4",
            "five":"5",
            "six":"6",
            "seven":"7",
            "eight":"8",
            "nine":"9",
            }
    array = ["1","2","3","4","5","6","7","8","9"]
    accumulator = 0
    reversed_string = ""
    for line in data:
        string = ""
        number = ""
        for char in line:
            string+=char
            if find_string(string=string,dict=dict) != None:
                number = dict[find_string(string=string,dict=dict)]
                break
            elif char in array:
                number = char
                break
        string = ""
        for x in range(-1,-len(line) - 1,-1):
            string+=line[x]
            reversed_string = string[::-1]
            if line[x] in array:
                number +=line[x]
                break
            elif find_string(string=reversed_string,dict=dict) !=None:
                number +=dict[find_string(string=reversed_string,dict=dict)]
                break
        accumulator+=int(number)
print(accumulator)

        
        
            
           