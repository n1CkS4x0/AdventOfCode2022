with open("1.txt","r") as f:
    
    file = f.readlines()
    total_calories = 0
    elfs = []
    
    for line in file:
        if line == "\n":
            elfs.append(total_calories)
            total_calories = 0
        else:
            total_calories += int(line)
                    
    print("solution 1: ", max(elfs))
    elfs = sorted(elfs)[-3:]
    print("solution 2: ", sum(elfs))
    