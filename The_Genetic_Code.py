inlines = open("dict.txt","r").read().splitlines()
#close("dict.txt")
#temp = [line[:-1] for line in inlines]

proDict = {}
for line in inlines:
    tempData = line.split("   ")
    for data in tempData:
        if data:
            dictData = data.split(" ")
            proDict[dictData[0]] = dictData[1]

del tempData
del dictData
print("data collected")
proline = open("input.txt", "r").read()
#close("input.txt")
codeName =""
i=0
j=0
while i < len(proline)-4 :
    if proline[i:i+3] != "Stop":
        codeName += proDict[proline[i:i+3]]
    i+=3
    j+=1
 
open("output.txt","w").write(codeName)