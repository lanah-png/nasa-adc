#get coords for mesh generation

file = open("squarefulldatascale1.txt", "r")
s = file.read().split("\n")

out = open("coords.txt", "a")

size = len(s)

#separate txt file by linebreaks

for x in range(0, size-1):
    values = s[x].split(",")
    for y in range(0, size-1):
        if values[y] != "nan":
            out.write(str(x)+" "+str(y)+" "+values[y]+"\n")

out.close()
