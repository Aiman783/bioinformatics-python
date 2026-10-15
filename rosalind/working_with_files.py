with open(r"C:\Users\aiman\Downloads\rosalind_ini5 (1).txt", "r") as infile:
    lines = infile.readlines()

with open("output.txt", "w") as outfile:
    for i in range(len(lines)):
        if (i + 1) % 2 == 0:
            outfile.write(lines[i])
            print(lines[i], end = "")
