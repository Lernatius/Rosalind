f = open("source.txt", "r")

DNA = f.read()
RNA = DNA.replace("T","U")


w = open("output.txt","w")

w.write(RNA)

f.close
w.close