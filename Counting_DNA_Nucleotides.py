f = open("source.txt", "r")
DNA = f.read()
numbers = [0,0,0,0]

sub = "A"
numbers[0]=DNA.count(sub, 0,-1)
sub = "C"
numbers[1]=DNA.count(sub, 0,-1)
sub = "G"
numbers[2]=DNA.count(sub, 0,-1)
sub = "T"
numbers[3]=DNA.count(sub, 0,-1)

print (str(numbers[0])+" "+str(numbers[1])+" "+str(numbers[2])+" "+str(numbers[3]))

