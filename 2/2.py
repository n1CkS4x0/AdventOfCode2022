def score1(line):
    if line == "A X":   return 1 + 3
    elif line == "A Y": return 2 + 6
    elif line == "A Z": return 3
    elif line == "B X": return 1
    elif line == "B Y": return 2 + 3
    elif line == "B Z": return 3 + 6
    elif line == "C X": return 1 + 6
    elif line == "C Y": return 2
    else: return 3 + 3
    
def score2(line):
    if line == "A X":   return score1("A Z")
    elif line == "A Y": return score1("A X")
    elif line == "A Z": return score1("A Y")
    elif line == "B X": return score1("B X")
    elif line == "B Y": return score1("B Y")
    elif line == "B Z": return score1("B Z")
    elif line == "C X": return score1("C Y")
    elif line == "C Y": return score1("C Z")
    else: return score1("C X")
    
def part1(file): return sum(map(lambda line: score1(line.strip()), file))
def part2(file): return sum(map(lambda line: score2(line.strip()), file))

exercises = [1,2]

for exercise in exercises:
    with open(f"{exercise}.txt","r") as f:
        
        all_file_lines = f.readlines()
        print(f"solution {exercise}: ", eval(f"part_{exercise}(all_file_lines)"))
        f.close
        
        