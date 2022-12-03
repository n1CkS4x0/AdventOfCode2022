alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_dict = {char_ : (i + 1) for i, char_ in enumerate(alphabet)}

def first_of_set(set_):
    return list(set_)[0]

def part_1(line):
    line = line.strip()
    half = len(line)//2
    
    first_half_line = set(line[:half])
    second_half_line = set(line[half:])
    
    set_intersection = first_half_line.intersection(second_half_line)
    return first_of_set(set_intersection)

def part_2(group_of_3):
    set_list = list(map(lambda line : set(line.strip()), group_of_3))
    return first_of_set(set.intersection(*set_list))

with open("1.txt","r") as f:
    file = f.readlines()
    print("sol1 :", sum(map(lambda x : alphabet_dict[part_1(x)],f)))    
    f.close()
    
with open("2.txt","r") as f:
    file = f.readlines()
    print("sol2 :",sum([alphabet_dict[part_2(file[i:i+3])] for i in range(0, len(file), 3)])) 
    f.close()