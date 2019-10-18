import operator

with open("input.txt","r") as f:
    lines = f.read().splitlines()
    DNAList = list()  #* f.read().count(">")
    f.close()

tempDNA = " " # Temporary variable to keep DNA code until transferring to the list

for line in lines :
    if line.startswith(">") :
        if not tempDNA == " ":
            DNAList.append(tempDNA)
            tempDNA = " "
            
    elif not line.startswith(">"):
        tempDNA += line



aLine = [0]*len(DNAList[1])
cLine = [0]*len(DNAList[1])
gLine = [0]*len(DNAList[1])
tLine = [0]*len(DNAList[1])

ancient =""
for linet in DNAList:     
    for index in range(len(linet)):
        if linet[index] == "A":
            aLine[index] += 1
        elif linet[index] == "C":
            cLine[index] += 1
        elif linet[index] == "G":
            gLine[index] += 1
        elif linet[index] == "T":
            tLine[index] += 1

with open("output.txt","a") as w:
    for comp in range(len(aLine)):

        dList = [aLine[comp], cLine[comp], gLine[comp], tLine[comp]]
        champ, value = max(enumerate(dList), key=operator.itemgetter(1))
       # champ = max(enumerate(dList))
        
        if champ == 0 :
            w.write("A")
        elif champ == 1:
            w.write("C")
        elif champ == 2:
            w.write("G")
        elif champ == 3:
            w.write("T")


    w.write("\n")    
    w.write("A:")
    for count in aLine:
        w.write(" "+str(count))

    w.write("\n")
    w.write("C:")
    for count in cLine:
        w.write(" "+str(count))

    w.write("\n")
    w.write("G:")
    for count in gLine:
        w.write(" "+str(count))

    w.write("\n")
    w.write("T:")
    for count in tLine:
        w.write(" "+str(count))

    w.write("\n")
    w.close()