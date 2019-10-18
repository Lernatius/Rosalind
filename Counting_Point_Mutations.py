lines = open("input.txt","r").readlines()

count = 0
for i in range(len(lines[1])):
    if lines[0][i] != lines[1][i]:
        count+=1
    

print(count)