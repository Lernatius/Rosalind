inlines = open("input.txt","r").read().splitlines()

counts = []
for i in range(len(inlines[0])):
    if inlines[0][i:].startswith(inlines[1]):
        counts.append(i+1)

print(counts)

w = open("output.txt","a")
for item in counts:
    w.write(str(item)+" ")

w.close()