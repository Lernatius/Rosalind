with open("input.txt","r") as f:
    lines = f.read().splitlines()
    f.close()
#import all the file and close


head = list()
DNA =    list()
tempDNA =""
for line in lines:
    if line.startswith(">"):
        head.append(line[1:])
        if not tempDNA == "":
            DNA.append(tempDNA)
            tempDNA =""
    elif (not line.startswith(">")) or (not line.empty()):
        tempDNA +=line
        if line == lines[-1]:
             DNA.append(tempDNA)




with open("output.txt","a") as w:
    for index in range(len(head)):
        for index2 in range(len(DNA)):
            if index != index2:
                if DNA[index][-3:] == DNA[index2][:3]:
                    print(head[index] + " " + head[index2])
                    w.write(head[index] + " " + head[index2] + "\n")


