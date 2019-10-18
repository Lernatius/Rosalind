f = open("source.txt", "r")

DNA = f.read()
Complemented = DNA[::-1]

w = open("output.txt","w")
newstring = []
for x in list(Complemented):
    if x == "A":
        newstring.append("T")
    elif x == "C":
        newstring.append("G")
    elif x == "G":
        newstring.append("C")
    elif x == "T":
        newstring.append("A")

w.write(str("".join(newstring)))

f.close
w.close
