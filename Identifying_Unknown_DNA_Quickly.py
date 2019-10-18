f = open("input.txt","r").readlines()
w = open("output.txt","w")

class DNA :
    def __init__(label, content):
        self.label = label
        self.content = content
    

tempName =[]
tempContent = []
started = False
tempDict = {}


for line in f:
    newLine = line.strip()

    if newLine[0] == ">":
        tempName = newLine[1::]
        started = True
    elif newLine[0] == ">" and started == True and tempContent != []:
        tempDict[tempName] = tempContent
        tempName = newLine[1::]
        tempContent = []
    elif newLine[0] != ">" :
        tempContent += newLine


for n in tempDict:
    w.writeline(n.name)
    w.writelines(n.content)


