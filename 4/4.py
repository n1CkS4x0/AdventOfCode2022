
with open("1.txt","r") as f:
    total = 0
    for line in f:
        line = line.strip()
        first_range, second_range = line.split(",")
        begin_first_range, end_first_range = map(int,first_range.split("-"))
        begin_second_range, end_second_range = map(int,second_range.split("-"))
        if (begin_first_range >= begin_second_range and end_first_range <= end_second_range) \
            or (begin_second_range >= begin_first_range and end_second_range <= end_first_range):
          total += 1
    print(total)      


with open("2.txt","r") as f:
    total = 0
    for line in f:
        line = line.strip()
        first_range, second_range = line.split(",")
        begin_first_range, end_first_range = map(int,first_range.split("-"))
        begin_second_range, end_second_range = map(int,second_range.split("-"))
        if (begin_second_range <= begin_first_range <= end_second_range or begin_second_range <= end_first_range <= end_second_range) \
            or (begin_first_range <= begin_second_range <= end_first_range or begin_first_range <= end_second_range <= end_first_range):
          total += 1
    print(total)   

            
        