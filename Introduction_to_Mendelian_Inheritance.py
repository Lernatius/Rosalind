pop = open("input.txt","r").read().strip().split(" ")
nr = [0,0,0]
for i in range(len(pop)):
    nr[i]= int(pop[i])

k,m,n = nr[0],nr[1],nr[2]
prob = 1 - ((n*(n-1))+((m)*(m-1)/4) +(n*m))/((k+m+n)*(k+m+n-1))  

open("output.txt","w").write(str(prob))                                                      
print(prob)
close("input.txt")
close("output.txt")
